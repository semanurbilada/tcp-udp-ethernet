<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/919/919855.png" width="100" height="100" alt="icon">
<img src="https://cdn-icons-png.flaticon.com/512/8284/8284643.png" width="100" height="100" alt="icon">
</div>

<h1 align="center">TCP / UDP Ethernet</h1>

* [Purpose](#purpose)
* [Features](#features)
    * [Prerequisites](#prerequisites)
    * [Notes](#notes)
* [Project Structure](#project-structure)
* [Raspberry Pi](#raspberry-pi)
    * [How To Run?](#how-to-run)
* [Preview](#preview)
* [License](#license)
* [References](#references)

## Purpose
<div align="justify">

This project aims to measuring TCP/UDP protocol performance with Python in Raspberry Pi 4 via Ethernet connection.
- TCP: Transmission Control Protocol
- UDP: User Datagram Protocol

## Features
- Both TCP/UDP Client and Server
- Performance Measurement: Latency - Throughput - Reliability

### Prerequisites
* Ethernet cable and Modem
* Raspberry Pi 4 (4GB at least)
* SD Card (32GB at least) and reader

### Notes
1. I initially tested with C-based implementations but did not achieve effective results.<br>Therefore, I focused on Python-based UDP packet transmission.

</div>

## Project Structure

The project follows this directory structure:

```
tcp-udp-ethernet/
├── client/
│   ├── tcp_client.py
│   ├── udp_client_packet.py
│   └── udp_client.py
│
├── server/
│   ├── tcp_server.py
│   ├── udp_server_packet.py
│   └── udp_server.py
│
├── test/
│   ├── test_client.c
│   └── test_server.c
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- client/: Contains client side codes.
- server/: Contains server side codes.
- test/: Contains test codes written in C.
- requirements.txt: Lists project dependencies.

## Raspberry Pi

### How To Run?
1. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

2. Run (example):
```
python3 tcp_server.py
```
and
```
python3 tcp_client.py
```


## Preview

<div align="center">
   
   ![Screenshot 2024-12-24 at 8 56 07 PM](https://github.com/user-attachments/assets/bb1616d5-f062-42d0-a15e-d433a5bef050)
</div>


## References

- https://docs.python.org/3/library/zlib.html
- https://wiki.python.org/moin/TcpCommunication
- https://wiki.python.org/moin/UdpCommunication
- https://www.geeksforgeeks.org/cyclic-redundancy-check-python/


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/semanurbilada/tcp-udp-ethernet?tab=MIT-1-ov-file#readme) file for details.
