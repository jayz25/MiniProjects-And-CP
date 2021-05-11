import socket
import sys

HEADER = 64
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket Object Creation
PORT = 9999 #Assigning Port
HOST = socket.gethostbyname(socket.gethostname()) #Getting host IP
print(HOST)
FORMAT = 'utf-8'
ADDR = (HOST, PORT)
SOCKET.bind(ADDR) #binding socket to IP and PORT

DISCONNECT_MSG = '!DISCON'  
def server_listen():
    print("[STARTING]..")
    SOCKET.listen() #listening to connections
    
     # Accepting connections which conn is object of socket and address is Address of connection
    
    #    print("[CONNECTED] ",addr)
    while True:
        conn, addr = SOCKET.accept()
        print(f"Connection Establised {conn} {addr}")
        #data = conn.recv(1024).decode(FORMAT) #Receing Data from client the parameter '5' means number of bad connections attempted before failure
        '''if not data:
            break
        if data == DISCONNECT_MSG:
            print("Disconnecting... ")
            break
        print(f" {[addr]}: {data} ")
    print("Out Of Loop")'''
    

        send_commands(conn)
        conn.close()        

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == DISCONNECT_MSG:
            conn.close()
            SOCKET.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),'utf-8')
            print(client_response, end='')


server_listen()