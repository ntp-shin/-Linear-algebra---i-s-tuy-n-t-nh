from traceback import print_tb
import numpy as np
import copy
# Gauss function
# Ladder Matrix

class MyMatrix:
    def __init__(self, input):
        matrix = []
        for row in input:
            temp = []
            for value in row:
                temp.append(float(value))
            matrix.append(temp)
    
        self.root = np.array(matrix)
        self.matrix = np.array(matrix)
        self.numRow = len(matrix)
        self.numCol = len(matrix[0])
        self.solutions = []

        for i in range(self.numCol - 1):
            self.solutions.append(None)
        print(self.solutions)
    def clear(self):
        self.root = None
        self.matrix = None
        self.inv = None
        self.numRow = 0
        self.numCol = 0
    @staticmethod
    def swapRow(matrix, row1, row2):
        matrix[[row1, row2]] = matrix[[row2, row1]]

    @staticmethod
    def mulRow(matrix, k: float, row):
        numRow = len(matrix)
        numCol = len(matrix[0])
        if k == 0:
            print("He so phai khac 0")
            return
        if row < 0 or row > numRow:
            print("Hang khong ton tai") 
            return

        for i in range(numCol):
            matrix[row][i] = (matrix[row][i]) * k
        return

    @staticmethod
    def plusRow(matrix, rowI, k: float, rowJ):
        numRow = len(matrix)
        numCol = len(matrix[0])
        if not (0 <= rowI, rowJ <= numRow):
            print("Hang khong hop le")
            return
    
        for i in range(numCol):
            matrix[rowI][i] += k * matrix[rowJ][i]
        return

    def printMatrix(self):
        print(self.root)

    def Gauss_elimination(self):
        self.matrix = copy.deepcopy(self.root)
        for i in range(self.numRow):
            if self.matrix[i][i] == 0:
                for j in range(i + 1, self.numRow):
                    if self.matrix[j][i] != 0:
                        self.swapRow(self.matrix, i, j)
                        break
            if abs(self.matrix[i][i]) < 0.00001:
                continue
            self.mulRow(self.matrix, 1 / self.matrix[i][i], i)
            for j in range(self.numRow):
                if j != i:
                    self.plusRow(self.matrix, j, -self.matrix[j][i], i)

        for i in range(self.numRow):
            for j in range(i + 1, self.numRow):
                for k in range(self.numCol):
                    if self.matrix[i][k] == 0 and self.matrix[j][k] != 0 and self.matrix[i][i] == 0:
                        self.swapRow(self.matrix, i, j)
        return self.matrix

A = [[1, 2, -1, -1],[2, 2, 1, 1], [3, 5, -2, -1],  [3, 5, -2, -1]]
B = [[0, 0, -2, 0, 7, 12], [2, 4, -10, 6, 12, 28], [2, 4, -5, 6, -5, -1]]
Amatrix = MyMatrix(A)
print(Amatrix.root)
print('\n')
print(Amatrix.Gauss_elimination())