#Phan ra QR - 
from cmath import sqrt
import copy

def convertMatrix(matrix):
    numRow = len(matrix)
    numCol = len(matrix[0])
    newMatrix = []
    for j in range(numCol):
        colum = []
        for i in range(numRow):
            colum.append(float(matrix[i][j]))
        newMatrix.append(colum)
    return newMatrix

def convert(matrix):
    numRow = len(matrix)
    numCol = len(matrix[0])
    newMatrix = []
    for j in range(numCol):
        colum = []
        for i in range(numRow):
            colum.append(matrix[i][j])
        newMatrix.append(colum)
    return newMatrix

def mulVectorWithNumber(vector, number):
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * number)
    return result

def mulTwoVector(vector1, vector2):
    result = 0
    if len(vector1) != len(vector2):
        return -1
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

def minusTwoVector(vector1, vector2):
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] - vector2[i])
    return result

def proj(u, v):
    result = copy.deepcopy(u)
    heso = mulTwoVector(u, v) / mulTwoVector(u, u)
    for i in range(len(u)):
        result[i] = u[i] * heso
    return result

def GramSchmidt(matrixInput):
    matrix = convertMatrix(matrixInput)
    numRow = len(matrix)
    numCol = len(matrix[0])

    resultMatrix = []
    u0 = matrix[0]
    v0 = mulVectorWithNumber(u0, 1 / sqrt(mulTwoVector(u0, u0)))
    resultMatrix.append(v0)
    for i in range(1, numRow):
        ui = matrix[i]
        for j in range(0, i):
            ui = minusTwoVector(ui, proj(resultMatrix[j], ui))
        vi = mulVectorWithNumber(ui, 1 / sqrt(mulTwoVector(ui, ui)))
        resultMatrix.append(vi)
    return convert(resultMatrix)

def findQR(matrixInput):
    matrix = convertMatrix(matrixInput)

    Q = GramSchmidt(matrixInput)
    Qconvert = convert(Q)
    R = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            if j < i:
                row.append(0)
            else:
                row.append(mulTwoVector(Qconvert[i], matrix[j]))
        R.append(row)
    return Q, R

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
        print()
    
A = [[1, 1, 1], [2, -2, 2], [1, 1, -1]]
Q, R = findQR(A)
printMatrix(Q)
print()
printMatrix(R)