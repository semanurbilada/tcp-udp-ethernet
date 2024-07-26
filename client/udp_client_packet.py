import socket
import struct
import time
import zlib

def create_message(seq, end, timestamp, message):
    # Ensure the message is exactly 60 bytes
    message = message.ljust(60)[:60]
    # Combine the components of packets into a single message
    # It contains sequence identifier (S and E), timestamp, fixed-length message
    data = struct.pack('!2c1b1d60s', seq, end, 0, timestamp, message.encode('utf-8'))
    # Calculate the CRC32
    crc = zlib.crc32(data) & 0xffffffff
    # Append the CRC to the data
    return data + struct.pack('!I', crc)

def udp_client(server_ip, port, message_count):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        for i in range(message_count):
            timestamp = time.time()
            message = f"Hello Server, this is message {i+1}"
            packet = create_message(b'S', b'E', timestamp, message)
            
            s.sendto(packet, (server_ip, port))
            print(f"Message {i+1} sent with timestamp {timestamp}")

            response, _ = s.recvfrom(1024)
            print(f"Response from server: {response}\n")

    except Exception as e:
        print(f"Error connecting to client: {e}")

    finally:
        s.close()
        print("Socket closed")

# Change port, ip and message count and call the func
udp_client(port = 12345, server_ip = 'server_ip', message_count=1000)