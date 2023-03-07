def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

def alphaDecrypt(message, alpha):
    decryptArray=[]
    for char in list(message):
        decryptArray.append(get_keys_from_value(alpha, char)[0])
    return "".join(decryptArray)

