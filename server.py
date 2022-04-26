from operator import truediv
from re import S
import threading
import socket
import threading
HEADER=64
port=5050
SERVER=socket.gethostbyname(socket.gethostname())
FORMAT='utf-8'
DISCONNEST_MSG='!DISCONNECT'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR=(SERVER , port)
server.bind(ADDR)


def handle_client (conn,ADDR):
    print(f"[NEW CONNECTION] {ADDR} connected \n")
    connected=True
    while connected:
         msg_length=conn.recv(HEADER).decode(FORMAT)
         if msg_length:
            msg_length= int (msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNEST_MSG:
               connected=False
            print(f"[{ADDR}] {msg}")  
            conn.send("MSG received".encode(FORMAT)) 
    conn.close()      



def start():
    server.listen()
    print(f"[LISTENNING] Server is listenning on {SERVER}")  
    while True:
        conn , addr =server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")  


print ("[STARTING] server is starting.....")    
start() 