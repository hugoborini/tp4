import sys
sys.path.insert(1, 'lib')
from lib import alpha
from lib import cesar
from lib import transpositionCipher
import re

def deChrifKey(key):
    chunkTab2d=[]
    alphaTabDecrypt={}
    keyTab=list(key)
    for i in range(0, 4):
        del keyTab[0]


    key="".join(keyTab)

    keyTransArray = re.split("--[\/, @, #, =, ! ]é", key)
    keyTrans = keyTransArray[len(keyTransArray) - 1]
    del keyTransArray[len(keyTransArray) - 1]
    key = "".join(keyTransArray)


    decalageTab=re.split("B[\/, @, #, =, ! ]", key)
    decalage = decalageTab[len(decalageTab) - 1]
    del decalageTab[len(decalageTab) - 1]
    key = "".join(decalageTab)


    keyTab = re.split("\/[=, #, @, \/, !]>", key)


    i=0
    for chunk in keyTab:
        i = i + 1
        chunkTab = list(chunk)

        if i % 2 == 0:
            del chunkTab[0]

        else:
            for y in range(0, len(chunkTab)):
                if y !=0:
                    del chunkTab[1]

        chunkTab2d.append(chunkTab)

    j = 0
    entryHistory=""
    for charArray in chunkTab2d:
        for char in charArray:
            j = j + 1

            if j % 2 == 0:
                alphaTabDecrypt[entryHistory] = char
            else:
                alphaTabDecrypt[char] = "test"
                entryHistory=char




    return {
        "newAlpha": alphaTabDecrypt,
        "decalage": decalage,
        "keyTrans": keyTrans

    }



def myDecrypt(message, key):

    info = deChrifKey(key)



    message = alpha.alphaDecrypt(message, info["newAlpha"])
    message = transpositionCipher.decryptTrans(message, info["keyTrans"])
    message = cesar.cesarDecrypt(message, info["decalage"])



    return message

