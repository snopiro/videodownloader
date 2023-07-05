###########################################
# Main Runner for downloader
###########################################

import javguru_curl_extractor as jgce

# Get the URL from the user
url = input("Paste the URL: ")

#run the uip bat using the user's url
jgce.run_uip_bat(url)

#run the downloader
exec(open("javguru_downloader.py").read())