from unittest import result
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv('wine.csv', sep=';')

# Title "fixed acidity" // "volatile acidity" // "citric acid" // "residual sugar" //
# "chlorides" // "free sulfur dioxide" // "total sulfur dioxide" // 
# "density" // "pH" // "sulphates" // "alcohol" // "quality"
def createMatrix(data, titles):
    colum0 = data[titles[0]]

    if colum0 is None:
        return None

    matrix = np.array([colum0]).T
    colum0 = np.array([colum0]).T

    num = len(titles)
    for i in range(1, num):
        title = titles[i]
        if title == None:
            ones = np.ones(colum0.shape, dtype=np.int8)
            matrix = np.concatenate((matrix, ones), axis= 1)
        else:
            colum = np.array([data[title]]).T
            matrix = np.concatenate((matrix, colum), axis= 1)
    return matrix

def matrixResult(data, title):
    colum = np.array([data[title]]).T
    return colum

def LinearRegression(matrix, result):
    # x = (A.T * A)^-1 * A.T * b = [a b] trong y =ax + b
    #x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
    x = np.linalg.inv(matrix.transpose().dot(matrix)).dot(matrix.transpose()).dot(result)
    return x

def leastSquares(data, title, titleResult):
    xColum = data[title]
    yColum = matrixResult(data, titleResult)
    matrix = createMatrix(data, [title, None])

    ab = LinearRegression(matrix, yColum)
    a = ab[0][0]
    b = ab[1][0]
    x0 = xColum
    y0 = a * x0 + b
    leastSquares = 0
    for i in range(len(yColum)):
        leastSquares += (y0[i] - yColum[i][0]) ** 2
    print("__ Least Squares of " + title + " = ", int(leastSquares))
    return leastSquares

def drawLinearRegression(data, title, titleResult):
    xColum = data[title]
    yColum = matrixResult(data, titleResult)
    matrix = createMatrix(data, [title, None])
    xMin = min(xColum)
    xMax = max(xColum)
    
    plt.title(title)
    plt.plot(xColum, yColum, 'go')
    plt.xlabel("number of " + title)
    plt.ylabel("quality")

    ab = LinearRegression(matrix, yColum)
    a = ab[0][0]
    b = ab[1][0]
    x0 = np.linspace(xMin, xMax, 100000)
    y0 = a * x0 + b
    plt.plot(x0, y0, 'r')
    plt.show()    



A = [1, 2, 3]
m = [[2, 3, 5], [1, 2, 3], [1, 2, 3]]
titles = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
Matrix = createMatrix(df, titles)
# print(Matrix)
MatrixResult = matrixResult(df, "quality")
x = LinearRegression(Matrix, MatrixResult)
print(x)
leastSquares(df, "fixed acidity", "quality")
leastSquares(df, "volatile acidity", "quality")
leastSquares(df, "citric acid", "quality")
leastSquares(df, "residual sugar", "quality")
leastSquares(df, "chlorides", "quality")
leastSquares(df, "free sulfur dioxide", "quality")
leastSquares(df, "total sulfur dioxide", "quality")
leastSquares(df, "density", "quality")
leastSquares(df, "pH", "quality")
leastSquares(df, "sulphates", "quality")
leastSquares(df, "alcohol", "quality")
# print(x)
drawLinearRegression(df, "fixed acidity", "quality")
drawLinearRegression(df, "volatile acidity", "quality")
drawLinearRegression(df, "citric acid", "quality")
drawLinearRegression(df, "residual sugar", "quality")
drawLinearRegression(df, "chlorides", "quality")
drawLinearRegression(df, "free sulfur dioxide", "quality")
drawLinearRegression(df, "total sulfur dioxide", "quality")
drawLinearRegression(df, "density", "quality")
drawLinearRegression(df, "pH", "quality")
drawLinearRegression(df, "sulphates", "quality")
drawLinearRegression(df, "alcohol", "quality")
