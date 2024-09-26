@echo off
set /p target="Enter the target contact name: "
set /p message="Enter the message: "
set /p n="Enter the number of messages to send: "


python "C:\Coding1\Coding\python\Automation\whatsapp_bot\wpbot.py" "%target%" "%message%" %n%
pause
