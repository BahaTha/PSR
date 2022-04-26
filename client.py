import socket

HEADER=64
port=5050
SERVER='172.18.3.218'

print(SERVER)
FORMAT='utf-8'
DISCONNEST_MSG='!DISCONNECT'
ADDR=(SERVER , port)


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send (send_length)
    client.send(message)
    print (client.recv(2048).decode(FORMAT))

send("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa khdem")    
input()
send("Helloo")    
input()