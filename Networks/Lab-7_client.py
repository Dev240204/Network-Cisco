import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 1111))
name = input("enter name: ")
c.send(bytes(name, "utf-8"))
print(c.recv(1024).decode())
c.close()
