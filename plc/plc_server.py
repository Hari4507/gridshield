import socket

HOST="0.0.0.0"
PORT=502

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((HOST,PORT))
sock.listen()

print("PLC server listening")

while True:

    conn,addr=sock.accept()

    data=conn.recv(1024)

    print("PLC received value:",data.decode())

    conn.close()