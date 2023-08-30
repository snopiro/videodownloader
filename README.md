# videodownloader
while i originally made this to download the chainsaw man AV, it'll work on any jav.guru video. Useful for downloading the entire HD quality video

Right now, you must create a requests.txt file and put it in the folder with the code.
You can get this by going to the video you want to download, open the debugger console, disable breakpoints, then open the video, select the quality and find the seg-#-blahblah ts file.
Right click it, copy all as curl request, and paste it into the requests.txt file (that you created), and run the file with "python main.py"


Main concepts of this code is grabbing all the relevant details about the url and headers so that the server will let you download, parametrizing it, and looping through to download every segment.
It implements threads to download multiple segments concurrently to speed up download speed (I think it speeds up at least), then uses ffmpeg to combine all the segments together.


# also if you're an employer looking at this
While this project's purpose is definitely NSFW, I believe there's at least some merit in the code being public and it was a pretty fun project to try to string UIPath together and python, so here it is
