from copy import deepcopy
import numpy as np
import random
maxRandom = 10

# Create random matrix n*n
def create_ramdom_matrix(n: int):
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(-maxRandom, maxRandom))
        m.append(row)
    return m

# Find multiplication of two matrices
def multiplyMatrix(m1, m2):
    numRow1 = len(m1)
    numCol1 = len(m1[0])
    numRow2 = len(m2)
    numCol2 = len(m2[0])
    if numCol1 != numRow2:
        print("Error: Matrix multiplication not possible")
        return None
    newMatrix = []
    for i in range(numRow1):
        row = []
        for j in range(numCol2):
            sum = 0
            for k in range(numCol1):
                sum += m1[i][k] * m2[k][j]
            row.append(round(sum, 10))
        newMatrix.append(row)
    return newMatrix

# Find exponentiation of matrix
def exponentMatrix(matrix, m: int):
    if m == 0:
        mt = deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i == j:
                    mt[i][j] = 1
                else:
                    mt[i][j] = 0
        return mt
    if m == 1:
        return matrix
    if m > 1:
        return multiplyMatrix(matrix, exponentMatrix(matrix, m - 1))
# Print matrix
def printMatrix(matrix):
    if matrix is None:
        print("Matrix is None")
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
        print()

m = [[1, 1/3, 1/2, 1/4, 0], [0, 0, 0, 1/4, 0], [0, 0, 0, 1/4, 0], [0, 1/3, 1/2, 0, 0], [0, 1/3, 0, 1/4, 1]]

print('\nMatrix A:')
printMatrix(m)
print()


matrix = np.array(m)
matrixN = np.linalg.matrix_power(matrix, 1000)
print(matrixN)

m0 = [[0], [1], [0], [0], [0]]
p0 = np.array(m0)
x = matrixN.dot(p0)
print(x)
# m0 = exponentMatrix(m, 0)
# print('\nMatrix A^0:')
# printMatrix(m0)


# import pandas as pd
# import numpy as np

# input = pd.read_csv('weights.csv', sep=',')
# def getFullTitles(data: pd):
#     titles = []
#     colums = data.columns
#     n = len(colums)
#     for i in range(n):
#         if i != 0 and i < n - 1:
#             titles.append(colums[i])
#     return titles

# def getResultTitle(data: pd):
#     colums = data.columns
#     return str(colums[-1])

# def createMatrix(data: pd, titles: list):
#     colum0 = data[titles[0]]

#     if colum0 is None:
#         return None

#     matrix = np.array([colum0]).T
#     colum0 = np.array([colum0]).T

#     num = len(titles)
#     for i in range(1, num):
#         title = titles[i]
#         if type(title) is list:
#             col = np.ones(colum0.shape, dtype=np.int8)
#             for t in title:
#                 temp = np.array([data[t]]).T
#                 col = col * temp
#             matrix = np.concatenate((matrix, col), axis= 1)
#         elif title == None:
#             ones = np.ones(colum0.shape, dtype=np.int8)
#             matrix = np.concatenate((matrix, ones), axis= 1)
#         else:
#             colum = np.array([data[title]]).T
#             matrix = np.concatenate((matrix, colum), axis= 1)
#     return matrix

# def matrixResult(data: pd, title: str):
#     colum = np.array([data[title]]).T
#     return colum

# def LinearRegression(matrix: np, result: np):
#     # x = (A.T * A)^-1 * A.T * b = [a b] trong y =ax + b
#     #x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
#     x = np.linalg.inv(matrix.transpose().dot(matrix)).dot(matrix.transpose()).dot(result)
#     return x

# def RSS(data: pd, titles: list, titleResult: str):
#     matrix = createMatrix(data, titles)
#     result = matrixResult(data, titleResult)
#     x = LinearRegression(matrix, result)
#     y = matrix.dot(x)
#     # return np.sum((y - result) ** 2)
#     rss = 0
#     for i in range(len(y)):
#         rss += (y[i][0] - result[i][0]) ** 2
#     return rss


# titles = getFullTitles(input)
# titles.append(['length','headc'])
# titleResult = getResultTitle(input)

# matrix = createMatrix(input, titles)
# Result = matrixResult(input, titleResult)
# print(matrix)

# for i in range(len(titles)):
#     if type(titles[i]) is list:
#         print('--->', titles[i])
#     else:
#         print(titles[i])

