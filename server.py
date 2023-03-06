import socket
import sys

###################### on definis notre hostname et le port pour le server
hostname="localhost"
port=1234

###################### recuperation de l'objet socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###################### configuration de la socket
sock.bind([hostname, port])
sock.listen(10)


while True:
    ###################### acceptation de la connection du client
    connection, client_address = sock.accept()

    ###################### recuperation du message du client
    welcome = connection.recv(1024)
    print(welcome.decode("utf-8"))