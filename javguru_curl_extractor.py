import subprocess
import json

def run_uip_bat(url): 
    batch_file_path = "uip.bat"  # Replace with the actual path to your batch file
    output_file_path = "request.txt"  # Replace with the desired output file path

    # Run the batch file with the URL as a command line argument and capture the output
    completed_process = subprocess.run([batch_file_path, url], shell=True, capture_output=True, text=True)

    # Extract the URL from the output
    output = completed_process.stdout.strip()
    data = json.loads(output)
    curl = data.get("out_curl_request", "")

    # Save the URL into the output file
    with open(output_file_path, "w") as output_file:
        output_file.write(curl)
