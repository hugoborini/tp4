import socket
import sys
sys.path.insert(1, 'lib')
from lib import cesar

###################### on definis notre hostname et le port pour le server
hostname="localhost"
port=1236

###################### recuperation de l'objet socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###################### configuration de la socket
sock.bind((hostname, port))
sock.listen(10)

key = ""
algo = ""
messageCrypt = ""

while True:

    ###################### acceptation de la connection du client
    connection, client_address = sock.accept()

    ###################### recuperation du message du client
    message = connection.recv(1024)
    message = message.decode("utf-8")


    if "key" in message:
        key = message.split(":")[1]
        connection.sendall("key recived".encode())

    if "algo" in message:
        algo = message.split(":")[1]
        connection.sendall("algo recived".encode())

    if "message" in message:
        connection.sendall("message recived".encode())
        messageCrypt = message.split(':')[1]
        print("message crypté : " + messageCrypt)

    if algo == "cesar":
        print("message decrypté : " + cesar.cesarDecrypt(messageCrypt, key))


