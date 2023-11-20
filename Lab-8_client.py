import socket

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddress = ('127.0.0.1', 12345)

while True:
    message = input("Enter message: ")
    UDPClientSocket.sendto(message.encode(), serverAddress)
    serverResponse, serverAddress = UDPClientSocket.recvfrom(1024)
    print(f"Received response: {serverResponse.decode()}")
    if message == "exit":
        break  
