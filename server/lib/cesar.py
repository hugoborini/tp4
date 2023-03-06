import string

def cesarDecrypt(message, decalage):
    decalage = int(decalage)
    alphabetArray=list(string.ascii_lowercase)
    cryptArray=[]
    for char in list(message):
        newIndex = alphabetArray.index(char) - decalage
        if newIndex <= 0:
            newIndex = newIndex + len(alphabetArray)

        cryptArray.append(alphabetArray[newIndex])

    return ''.join(cryptArray)


