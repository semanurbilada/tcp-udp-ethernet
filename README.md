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
* [Licence](#licence)

## Purpose
<div align="justify">

This project aims to measuring TCP/UDP protocol performance with Python in Raspberry Pi 4 via Ethernet connection.

## Features
### Prerequisites
* Ethernet cable and Modem
* Raspberry Pi 4 (4GB at least)
* SD Card (32GB at least) and reader

### Notes
1. 

</div>

## Project Structure

The project follows this directory structure:

```
tcp-udp-ethernet/
│
├── client/
│   └── client.py
│
├── server/
│   └── server.py
│
├── gitignore
├── README.md
└── requirements.txt
```

- client/: Contains ...
- server/: Contains ...
- requirements.txt: Lists project dependencies.

## Raspberry Pi

### How To Run?
1. Virtual environment setup:
```
python3 -m venv env
```

2. To activate the virtual environment (Windows):
```
env/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source env/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run:
```
python3 server.py
```
and
```
python3 client.py
```

## Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/semanurbilada/tcp-udp-ethernet?tab=MIT-1-ov-file#readme) file for details.