import os
import subprocess
import requests

#Change these to the specific video you want to download
base_url = ""
headers = {

}

download_directory = "./downloaded_files"
os.makedirs(download_directory, exist_ok=True)

# Download the files
for segment_number in range(1, 727):
    url = base_url.format(segment_number)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(download_directory, f'segment_{segment_number}.ts')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Segment {segment_number} downloaded successfully.')
    else:
        print(f'Failed to download segment {segment_number}. Status code: {response.status_code}')
        break

# Combine the downloaded files using FFmpeg
if segment_number == 726:
    input_directory = "./downloaded_files"
    output_directory = "./combined_video"
    os.makedirs(output_directory, exist_ok=True)

    i = 1
    ts_files = []

    while True:
        ts_filename = f"segment_{i}.ts"
        ts_filepath = os.path.join(input_directory, ts_filename)

        # Check if the .ts file exists
        if not os.path.exists(ts_filepath):
            break

        ts_files.append(ts_filepath)
        i += 1

    # Set the output file path
    output_filepath = os.path.join(output_directory, "joined_video.mp4")

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

    print("Joining completed!")
else:
    print("Download process failed. Skipping joining step.")