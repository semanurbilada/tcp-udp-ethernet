import time
import socket

# s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp

port = 12345
server_ip = 'server_ip'

s.connect((server_ip, port)) 
print(f"Connected to server at {server_ip}:{port}")

try:
    for i in range(100):
        timestamp = time.time()
        message = f'{timestamp} Hello this is your client! Message {i+1}'
        s.send(message.encode('utf-8'))
        print(f"Message {i+1} sent with timestamp {timestamp}")

        response = s.recv(1024)
        print(f"Response from server: {response.decode('utf-8')}\n")
finally:
    s.close()
    print("Socket closed")