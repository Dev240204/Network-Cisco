import socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddress = ('127.0.0.1', 12345)
UDPServerSocket.bind(serverAddress)

print("UDP server up and listening")

while True:
    message, address = UDPServerSocket.recvfrom(1024)
    print(f"Received message from {address}: {message.decode()}")
    reply = input("Enter your response: ")
    UDPServerSocket.sendto(reply.encode(), address)
