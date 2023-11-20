import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create socket object
print("socket created?")
s.bind(('127.0.0.1', 1111)) #bind to port
s.listen(5)
print("waiting for connection")
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode
    print ('got connection from ', addr)
    c.send(bytes("connection done", 'UTF-8'))
    c.close()
    break