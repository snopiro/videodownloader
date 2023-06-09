import os
import subprocess
import requests
import threading

def download_segment(segment_number, end_event):
    segment_url = url.replace("seg-2", f"seg-{segment_number}")
    print("Downloading: " + segment_url)
    response = requests.get(segment_url, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(download_directory, f's{segment_number}.ts')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Segment {segment_number} downloaded successfully.')
    elif response.status_code == 404:
        print(f'Status code: {response.status_code}. Reached end of segments for thread {threading.current_thread().name}.')
        end_event.set()  # Set the event to signal the end of segments
    else:
        print(f'Failed to download segment {segment_number}. Status code: {response.status_code} for thread {threading.current_thread().name}.')

# Read the URL and headers from the file
with open("request.txt", "r") as file:
    url = file.read()

print("URL: " + url)

headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Origin": "https://javplaya.com",
    "Referer": "https://javplaya.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

download_directory = ".\d"
os.makedirs(download_directory, exist_ok=True)

# Download the files using threading
segment_number = 1
threads = []
max_threads = 5  # Maximum number of simultaneous downloads

end_event = threading.Event()  # Event to signal the end of segments

while True:
    # Check if the maximum number of threads is reached
    if len(threads) >= max_threads:
        # Wait for any of the running threads to complete
        for thread in threads:
            thread.join()
            threads.remove(thread)
        continue

    # Check if the end of segments is reached
    if end_event.is_set():
        break

    # Create a new thread for the segment download
    thread = threading.Thread(target=download_segment, args=(segment_number, end_event))
    thread.start()
    threads.append(thread)

    segment_number += 1

# Wait for all remaining threads to complete
for thread in threads:
    thread.join()

print("All segments downloaded!")

# Combine the downloaded files using FFmpeg
output_directory = ".\combined_video"
os.makedirs(output_directory, exist_ok=True)

i = 1
ts_files = []

while True:
    ts_filename = f"s{i}.ts"
    ts_filepath = os.path.join(download_directory, ts_filename)

    # Check if the .ts file exists
    if not os.path.exists(ts_filepath):
        break

    ts_files.append(ts_filepath)
    i += 1

# Set the output file path
output_filepath = os.path.join(output_directory, "Video.mp4")

# Prepare the ffmpeg command
ffmpeg_command = [
    "ffmpeg",
    "-i",
    "concat:" + "|".join(ts_files),
    "-c",
    "copy",
    output_filepath
]

# Execute the ffmpeg command
subprocess.run(ffmpeg_command)

# Clean up loose segment files
for ts_file in ts_files:
    os.remove(ts_file)

print("Loose segment files cleaned up.")