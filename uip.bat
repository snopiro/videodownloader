@echo off
set url=%1
"path\to\UiPath\Studio\UiRobot.exe" -file "JavGuruCurlRequest\JavGuruCurlRequest.1.0.6.nupkg" --input "{'in_url' : '%url%'}"
