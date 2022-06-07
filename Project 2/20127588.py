import numpy as np


class MyMatrix:
    def __init__(self, matrix):
        self.root = np.array(matrix)
        self.matrix = np.array(matrix)
        self.numRow = len(matrix)
        self.numCol = len(matrix[0])
        self.inv =  np.identity(self.numRow)

A = [[1, 2, 1], [3, 7, 3], [2, 3, 4]]
B = [[1, -1, 2], [1, 1, -2], [1, 1, 4]]
C = [[1, 2, 3], [2, 5, 3], [1, 0, 8]]
D = [[-1, 3, -4], [2, 4, 1], [-4, 2, -9]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

mtrix = MyMatrix(A)

mtrix.printMatrix()
print(mtrix.inverse())
print("\n A * A^-1 = I")
print(np.dot(A, mtrix.inverse()))
print("\n-------------------------\n")

mtrix.clear()
mtrix = MyMatrix(B)

mtrix.printMatrix()
print(mtrix.inverse())
print("\n B * B^-1 = I")
print(np.dot(B, mtrix.inverse()))
print("\n-------------------------\n")

mtrix.clear()
mtrix = MyMatrix(C)

mtrix.printMatrix()
print(mtrix.inverse())
print("\n C * C^-1 = I")
print(np.dot(C, mtrix.inverse()))
print("\n-------------------------\n")

# Do làm tròn nên kết quả nhân ma trận không còn chính xác
mtrix.clear()
mtrix = MyMatrix(D)

mtrix.printMatrix()
print(mtrix.inverse())
print("\n D * D^-1 = I")
print(np.dot(D, mtrix.inverse()))
print("\n-------------------------\n")