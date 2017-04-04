import socket,threading
from time import localtime, strftime

HOST = ''
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
user=[]
print("Start Server")

def serv(c):
        name = c.recv(1024)
        name = name.decode("utf-8","ignore")
        print("[" + name + "] JOINED SERVER")
        while c:
                data = c.recv(1024)
                data = data.decode("utf-8","ignore")
                
                string = "[" + name + "] " + data
                print(string)
                string = string.encode("utf-8")
                
                for each in user:
                        if c != each:
                                each.send(string)

while 1:
        c, addr = s.accept()
        user.append(c)
        threading._start_new_thread(serv,(c,))
