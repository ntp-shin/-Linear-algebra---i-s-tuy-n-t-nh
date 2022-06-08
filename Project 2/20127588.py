import numpy as np

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
        self.inv =  np.identity(self.numRow)


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

    def inverse(self):
        if self.numRow != self.numCol:
            print("Khong phai ma tran vuong")
            return None
        
        if (self.matrix == self.inv).all():
            print("Hoan thanh")
            return self.inv

        for i in range(self.numRow):

            if self.matrix[i][i] == 0:
                for j in range(i + 1, self.numRow):
                    if self.matrix[j][i] != 0:
                        self.swapRow(self.matrix, i, j)
                        self.swapRow(self.inv, i, j)
                        break

            if abs(self.matrix[i][i]) < 0.00001:
                print("Khong co ma tran nghich dao")
                return None

            self.mulRow(self.inv, 1 / self.matrix[i][i], i)
            self.mulRow(self.matrix, 1 / self.matrix[i][i], i)
            for j in range(self.numRow):
                if j != i: 
                    self.plusRow(self.inv, j, -self.matrix[j][i], i)
                    self.plusRow(self.matrix, j, -self.matrix[j][i], i)
        return self.inv
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

mtrix.clear()
mtrix = MyMatrix(D)
mtrix.printMatrix()
print(mtrix.inverse())
print("\n-------------------------\n")