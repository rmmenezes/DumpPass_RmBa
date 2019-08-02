# :rat: DumpPass_RmBa :rat:
This code works on Windows operating systems (PT-BR) and collects already connected WiFi passwords and critical google chrome browser information such as "History, Saved Passwords, Last Searches".

You can use this code in two ways. The first is to use Python to run the code directly. However in environments that do not have the python interpreter available you can create a Windows executable (.EXE).

To create your executable (.EXE) file you can use a Python script converter in Windows executable programs that can run without requiring a Python installation. Some converter programs such as py2exe, cx_Freeze, PyInstaller. PyInstaller is recommended and it will be like this converter that we will follow this tutorial.

## PyInstaller Quickstart
To install PyInstaller you can use the following command:
```
python -m pip install pyinstaller
```

Once installed, use the command below in the current repository directory to convert the getwifipass.py and getgooglechromedump.py files to executable (.EXE).
```
pyinstaller --onefile getwifipass.py
```
```
pyinstaller --onefile getgooglechromedump.py
```

If everything is correct so far pyinstaller will create some folders and within "dist" you will find the executable file ready for use.

![img](autorun_img.PNG)
