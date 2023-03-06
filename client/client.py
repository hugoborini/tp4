import socket
import sys
import codecs
sys.path.insert(1, 'lib')
from lib import cesar

###################### on definis notre hostname et le port pour le server
hostname="localhost"
port=1236



def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to host')
    sock.connect((hostname, port))
    return sock

def send(command, sock):
    recv_data = ""
    data = True

    print('sending: ' + command)
    sock.sendall(command.encode())

    while data:
        data = sock.recv(1024)
        recv_data += data.decode("utf-8")
        print('received: ' + data.decode("utf-8"))

        sock.close()
        return recv_data



def sendMessage(hostname, port, message):
    sock = connect(hostname, port)
    send(message, sock)


############################ envoie d'un packet

key=4
algo="cesar"
message="hello"




sendMessage(hostname, port ,"key:4")
sendMessage(hostname, port ,"algo:cesar")
sendMessage(hostname, port ,"message:" + cesar.cesarEncrypt(message, key))