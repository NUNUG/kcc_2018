rem Find Python3 in one of these locations:
@echo off
echo Searching...

rem Python 3.6 installer, custom location, or by some other method (maybe older installers.
@dir /a "c:\python36\python?.exe

rem Python 3.6 installer, custom, all users.
@dir /a "c:\program files (x86)\python36-32\python?.exe"

rem Python 3.6 installer, default.  Does not put this in the path by default.  Can you believe it?
rem This equates to: "C:\Users\{yourname}\AppData\Local\Programs\Python\Python36-32"
dir /a "%localappdata%\programs\Python\Python36-32\python?.exe" 

echo Press ENTER...
pause >nul