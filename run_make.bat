@echo off
set "PATH=C:\Program Files (x86)\GnuWin32\bin;%PATH%"
set "PATH=C:\Program Files\nodejs;%PATH%"
set "PATH=%PATH%;C:\Users\erycl\AppData\Roaming\npm"
make %*
