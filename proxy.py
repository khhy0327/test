#-*- coding: utf-8 -*-
import winreg
import ctypes
import time
import sys
import webbrowser
import os
import PyV8

def refresh():
    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39
    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

root_key = winreg.HKEY_CURRENT_USER
sub_key = winreg.CreateKey(root_key, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")
winreg.SetValueEx(sub_key, 'AutoConfigURL', 0, winreg.REG_SZ, "https://pac.menlosecurity.com/goodmit-3f9bc7e03397/GIT001.dat")
print("enable")

#############################################################
# url = "http://www.naver.com"
# webbrowser.open(url, new=1, autoraise=True)

# os.system('explorer http://www.naver.com')

ctx = PyV8.JSContext()
ctx.enter()

js = """
window.open('http://www.naver.com','새창이름','scrollbars=yes,toolbar=yes,location=yes,resizable=yes,status=yes,menubar=yes,resizable=yes,width=100,height=100,left=0,top=0,fullscreen')
"""

ctx.eval(js)
#############################################################


time.sleep(10)

internet_set_option2 = ctypes.windll.Wininet.InternetSetOptionW
winreg.DeleteValue(sub_key, 'AutoConfigURL')
winreg.CloseKey(sub_key)
refresh()
print("disable")

# proxy2 = ("C:\Temp\dist\proxy2.exe")
# ctypes.windll.shell32.ShellExecuteA(0, 'open', proxy2, None, None, 1)

