import math
import random
import math

def encryptTrans(key,message):
    rows = math.ceil(len(message) / len(key))
    columns=len(key)
    pointer = 0
    encrypted = []
    matrix = [[''] * columns for i in range(rows)]

    for i in range(len(matrix)):
        for y in range(len(matrix[i])):

            if pointer >= len(message):
                matrix[i][y] = " "
            else:
                if message[pointer] == " ":
                    matrix[i][y] = " "
                else:
                    matrix[i][y] = message[pointer]

            pointer = pointer + 1




    for y in range(len(matrix[0])):
        for i in range(len(matrix)):
            encrypted.append(matrix[i][y])



    return "".join(encrypted)

