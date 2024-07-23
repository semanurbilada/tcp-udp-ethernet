import time
import socket

# UDP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("UDP Socket successfully created")

port = 12345
server_ip = 'ethernet_ip'

s.bind((server_ip, port))
print("Socket binded to %s" % port)

last_received_time = None

while True:
    try:
        data, addr = s.recvfrom(1024)
        print('Got connection from', addr)

        current_time = time.time()
        message = data.decode('utf-8')
        print(f"Message from client: {message}")

        # Calculate frequency based on timestamp
        if last_received_time is not None:
            elapsed_time = current_time - last_received_time
            frequency = 1 / elapsed_time if elapsed_time > 0 else float('inf')
            print(f"Timestamp: {current_time}, Frequency: {frequency:.2f} Hz\n")
        else:
            print(f"Timestamp: {current_time}, Frequency: N/A (first message)\n")

        last_received_time = current_time #calculating Hz based on received timestamp
        """
            1 Hz means one occurrence per second.
            1 kHz (kilohertz) equals 1,000 occurrences per second.
            1 MHz (megahertz) equals 1,000,000 occurrences per second.
            1 GHz (gigahertz) equals 1,000,000,000 occurrences per second.
        """
        response = 'Thank you for connecting!'
        s.sendto(response.encode('utf-8'), addr)

    except Exception as e:
        print(f"Error connecting to client: {e}")
    
    finally:
        print("DONE!")