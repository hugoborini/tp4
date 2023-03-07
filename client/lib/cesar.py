import string

def cesarEncrypt(message, decalage):
    alphabetArray=list(string.ascii_lowercase)
    alphabetArray.append(" ")
    cryptArray=[]
    for char in list(message):
        newIndex = alphabetArray.index(char) + decalage
        if newIndex >= len(alphabetArray):
            newIndex = newIndex - len(alphabetArray)

        cryptArray.append(alphabetArray[newIndex])

    return ''.join(cryptArray)


