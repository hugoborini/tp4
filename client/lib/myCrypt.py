import sys
sys.path.insert(1, 'lib')

from lib import cesar
from lib import alpha
from lib import transpositionCipher
import string
import random


############################## fonction qui genere une chaine de caractère aléatoire
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str





randomSign = ["@", "/", "#", "=", "!"]

########################################## fonction qui encrypte un message donner
def mycrypt(message, decalage, newAlpha):
    key=[]
    ##### encrypt en cesar
    message = cesar.cesarEncrypt(message, decalage)

    
    
    #####encrypt dans un nouvelle alphabet

    message = alpha.alphaCrypt(message, newAlpha)

    message = transpositionCipher.encryptTrans("hh", message)

    ##### creation de la clef
    randomIntSign = random.randint(0, len(randomSign) - 1)
    ###### ajoue d'un slug aléatoire au debut de la clef
    key.append(get_random_string(4))
    for alphaCar in newAlpha:
        randomInt = random.randint(4,9)
        randomIntSign = random.randint(0, len(randomSign) - 1)
        randomStr = get_random_string(randomInt)

        ##### ajoue du paterne de la clef
        key.append(alphaCar)
        key.append(randomStr)
        key.append("/" + randomSign[randomIntSign] + ">")
        key.append(str(randomInt))
        key.append(newAlpha[alphaCar])
        key.append("/" + randomSign[randomIntSign] + ">")

    randomIntSign = random.randint(0, len(randomSign) - 1)
    key.append("B" + randomSign[randomIntSign])
    key.append(str(decalage))
    key.append("--" + randomSign[randomIntSign] + "é")
    key.append("hh")




    return {
        "message": message,
        "key": "".join(key)
    }
