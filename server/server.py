import time
import socket

s = socket.socket()          
print("Socket successfully created")

port = 12345      
server_ip = 'ethernet_ip'

s.bind((server_ip, port)) 
print("Socket binded to %s" % port)

s.listen(5)
print("Socket is listening")       

while True: 
    c, addr = s.accept()      
    print('Got connection from', addr)

    last_received_time = None

    try:
        while True:
            message = c.recv(1024)
            if not message:
                break

            current_time = time.time()
            print(f"Message from client: {message.decode('utf-8')}")

            # Calculate frequency based timestamp
            if last_received_time is not None:
                elapsed_time = current_time - last_received_time
                frequency = 1 / elapsed_time if elapsed_time > 0 else float('inf')
                print(f"Timestamp: {current_time}, Frequency: {frequency:.2f} Hz\n")

                save_path = f"./saves/result.txt" #frequencies.txt file
            else:
                print(f"Timestamp: {current_time}, Frequency: N/A (first message)\n")

            last_received_time = current_time
            """
            1 Hz means one occurrence per second.
            1 kHz (kilohertz) equals 1,000 occurrences per second.
            1 MHz (megahertz) equals 1,000,000 occurrences per second.
            1 GHz (gigahertz) equals 1,000,000,000 occurrences per second.
            """
            response = 'Thank you for connecting!'
            c.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error connecting to client: {e}")

    finally:
        s.close()
        print("Connection closed")