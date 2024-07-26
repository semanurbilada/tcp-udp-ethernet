import socket
import struct
import time
import zlib

def udp_server(server_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    port = 12345
    server_ip = 'server_ip'

    s.bind((server_ip, port))
    print("UDP Socket successfully created and binded to port: ", port)
    
    while True:
        data, addr = s.recvfrom(1024)
        print('Got connection from', addr)
        
        # Unpack the data
        seq, end, zero, timestamp, message, received_crc = struct.unpack('!2c1b1d60sI', data)
        message = message.decode('utf-8').rstrip('\x00')

        # Recalculate the CRC to verify the data integrity
        crc = zlib.crc32(data[:-4]) & 0xffffffff
        
        if crc == received_crc:
            print(f"Message from client: {message}")
            print(f"Timestamp: {timestamp}")
            response = 'Thank you for connecting!'
            s.sendto(response.encode('utf-8'), addr)
        else:
            print("CRC check failed. Data may be corrupted.")