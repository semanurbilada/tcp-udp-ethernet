import time
import socket

# UDP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 12345
server_ip = 'server_ip'

try:
    for i in range(100):
        timestamp = time.time()
        message = f'{timestamp} Hello this is your client! Message {i+1}'

        s.sendto(message, (server_ip, port))
        print(f"Message {i+1} sent with timestamp {timestamp}")

        response = s.recvfrom(1024)
        print(f"Response from server: {response}\n")

except Exception as e:
        print(f"Error connecting to client: {e}")

finally:
    s.close()
    print("Socket closed")