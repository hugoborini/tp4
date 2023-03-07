import socket
import sys
sys.path.insert(1, 'lib')
from lib import cesar
from lib import myCrypt


#print(myCrypt.myDecrypt("1+@1ç%+$,@", "vxzjffjcfaoinu/@>94/@>dwqffopz/=>7,/=>budcd/@>4//@>eayppyreg/=>8#/=>hzyrn/=>4y/=>ghvvy//>46//>jcwtcajgpy//>9$//>asabdstn/#>7-/#>iurpvfjr//>7z//>xmewvurhwu//>99//>ldxrjrpet/#>8£/#>cvsescnv/!>7a/!>kidfhkiqsn//>9*//>mdtfxo/!>5?/!>nfgjbiuaqk/@>9!/@> mdgxkhszj/@>9>/@>obpmqi/@>5%/@>ppfwhz//>5.//>sagcjyft/@>7-/@>qhbxng/#>5ç/#>rzjzhz/@>51/@>uotzsp//>5X//>tekkrpp/#>62/#>wpxkmchuu/#>8_/#>zfitw/@>4</@>yzbrlmday/#>8@/#>visipyzg/=>7+/=>B=10--=éhh"))

#exit(0)

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


    if not messageCrypt == "":
        if algo == "cesar":
            print("message decrypté : " + cesar.cesarDecrypt(messageCrypt, key))
        elif algo == "myalgo":

            #print(myCrypt.myDecrypt(messageCrypt, key))
            print("message decrypté : " + myCrypt.myDecrypt(messageCrypt, key))


