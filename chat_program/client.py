import socket,threading
import tkinter

HOST = "127.0.0.1"
PORT = 8089      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send_msg():
        
        set_name = input("Input user name >>> ")
        name = set_name.encode("utf-8")
        s.send(name)
                
        while True:
                data = input()
                if not data:
                        continue
                data = data.encode("utf-8")
                s.send(data)
        s.close()
	
def get_msg():
	while True:
		data = s.recv(1024)
		data = data.decode("utf-8","ignore")
		print(data)
	s.close()


threading._start_new_thread(send_msg,())
threading._start_new_thread(get_msg,())

while True:
        pass
app = Tk()
app.geometry("800x600")
app.title("RootChat")
