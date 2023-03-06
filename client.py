import socket
import sys

###################### on definis notre hostname et le port pour le server
hostname="localhost"
port=1234


###################### recuperation de l'objet socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###################### connection au serveur socket
sock.connect([hostname, port])

############################ envoie d'un packet
sock.send("start !".encode())


