import socket
import sys
import codecs
sys.path.insert(1, 'lib')
from lib import cesar
from lib import myCrypt

###################### on definis notre hostname et le port pour le server
hostname="localhost"
port=1236


##################### notre alphabet crypté
newAlpha={
"f":"4",
"d":",",
"b":"/",
"e":"#",
"h":"y",
"g":"6",
"j":"$",
"a":"-",
"i":"z",
"x":"9",
"l":"£",
"c":"a",
"k":"*",
"m":"?",
"n":"!",
" ":">",
"o":"%",
"p":".",
"s":"-",
"q":"ç",
"r":"1",
"u":"X",
"t":"2",
"w":"_",
"z":"<",
"y":"@",
"v":"+",
}


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


message="hello world hugo aba"


info = myCrypt.mycrypt("hello hugo", 10, newAlpha)






sendMessage(hostname, port ,"key:" + info["key"])
sendMessage(hostname, port ,"algo:myalgo")
sendMessage(hostname, port ,"message:" + info["message"])