import random
from pprint import pprint
import numpy as np

data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

pprint(data)

result = []

A = [[9, -9, -4,  3,  6], [7, -3, -8,  4,  4], [7, -9,  1, -2,  8], [5, -3, -4, -9, -8], [8,  5, -5,  4,  6]]
DA1 = np.asarray(A)
print ('Diagonal (sum): ', np.trace(DA1))
print ('Diagonal (elements): ', np.diagonal(DA1))


A = [[9, -9, -4,  3,  6], [7, -3, -8,  4,  4], [7, -9,  1, -2,  8], [5, -3, -4, -9, -8], [8,  5, -5,  4,  6]]
DA2 = np.asarray(A)
DA2 = np.fliplr(DA2)
print ('Diagonal (sum): ', np.trace(DA2))
print ('Diagonal (elements): ', np.diagonal(DA2))

print(np.trace(DA1)+ np.trace(DA2))

result.append(np.trace(DA1)+ np.trace(DA2))

print(result)

B = [[ 2, -7,  2, -2,  0], [ 1,  8,  2,  2, -2], [ 6, -2,  5, -2,  5], [-4,  9, -5, -9, -7], [ 8,  0, -9,  2, -7]]
DB1 = np.asarray(B)
print ('Diagonal (sum): ', np.trace(DB1))
print ('Diagonal (elements): ', np.diagonal(DB1))


B = [[ 2, -7,  2, -2,  0], [ 1,  8,  2,  2, -2], [ 6, -2,  5, -2,  5], [-4,  9, -5, -9, -7], [ 8,  0, -9,  2, -7]]
DB2 = np.asarray(B)
DB2 = np.fliplr(DB2)
print ('Diagonal (sum): ', np.trace(DB2))
print ('Diagonal (elements): ', np.diagonal(DB2))

print(np.trace(DB1)+ np.trace(DB2))

result.append(np.trace(DB1)+ np.trace(DB2))

print(result)

C = [[-9,  5, -1,  9,  4], [ 3, -4, -6, -3,  3], [ 6,  6,  7, -3, -6], [-8,  9,  6, -1, -2], [-10, 2, -8, -4,  9]]
DC1 = np.asarray(C)
print ('Diagonal (sum): ', np.trace(DC1))
print ('Diagonal (elements): ', np.diagonal(DC1))

C = [[-9,  5, -1,  9,  4], [ 3, -4, -6, -3,  3], [ 6,  6,  7, -3, -6], [-8,  9,  6, -1, -2], [-10, 2, -8, -4,  9]]
DC2 = np.asarray(C)
DC2 = np.fliplr(DC2)
print ('Diagonal (sum): ', np.trace(DC2))
print ('Diagonal (elements): ', np.diagonal(DC2))

print(np.trace(DC1)+ np.trace(DC2))

result.append(np.trace(DC1)+ np.trace(DC2))

print(result)

print(min(result))