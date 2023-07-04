# videodownloader
while i originally made this to download the chainsaw man AV, the principle should work for any video on a website that gets the video as segments. (i think) but definitely works for jav.guru

Right now, you must create a requests.txt file and put it in the folder with the code.
You can get this by going to the video you want to download, open the debugger console, disable breakpoints, then open the video, select the quality and find the seg-#-blahblah ts file.
Right click it, copy all as curl request, and paste it into the requests folder, and run the file with "python main.py"
