import socket
import struct
import zlib
import time

def udp_server(server_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((server_ip, port))
    print("UDP Socket successfully created and binded to port", port)
    
    timestamps = []

    while True:
        data, addr = s.recvfrom(1024)
        print('\nGot connection from', addr)
        
        # Unpack the data with sequence identifier: S and E
        seq, end, zero, timestamp, message, received_crc = struct.unpack('!2c1b1d60sI', data)
        message = message.decode('utf-8').rstrip('\x00')

        # Recalculate the CRC to verify the data integrity
        crc = zlib.crc32(data[:-4]) & 0xffffffff
        
        # If CRC is correct, then print message and send response
        if crc == received_crc:
            print(f"Message from client: {message}")
            print(f"Sent Timestamp: {timestamp}")
            
            # Record the timestamp when the server receives the message
            received_time = time.time()
            timestamps.append(received_time)
            
            # Calculate and print the frequency if we have at least two timestamps
            if len(timestamps) > 1:
                time_differences = [t2 - t1 for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
                avg_time_difference = sum(time_differences) / len(time_differences)
                frequency = 1 / avg_time_difference
                print(f"Frequency: {frequency:.2f} Hz")
            
            response = 'Thank you for connecting!'
            s.sendto(response.encode('utf-8'), addr)
        else:
            print("CRC check failed. Data may be corrupted.")

# Change port, ip and call the func
udp_server(port = 12345, server_ip = 'server_ip')