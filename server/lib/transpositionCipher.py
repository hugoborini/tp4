import math

def decryptTrans(message, key):

    rows = math.ceil(len(message) / len(key))
    columns = len(key)
    decrypted = []

    # create a 2D array as a table
    matrix = [[''] * columns for i in range(rows)]
    pointer= 0

    for y in range(len(matrix[0])):
        for i in range(len(matrix)):

            if pointer >= len(message):
                break
            else:
                matrix[i][y] = message[pointer]
            pointer = pointer + 1


    for row in matrix:
        for columns in row:
            decrypted.append(columns)

    decrypted = "".join(decrypted)

    decrypted = decrypted.replace("_", " ")



    return decrypted

