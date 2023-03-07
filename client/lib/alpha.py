def alphaCrypt(message, alpha):
    cryptArray=[]
    for char in list(message):

        cryptArray.append(alpha[char])


    return "".join(cryptArray)

