from matrix.Matrix import Matrix
from vector.Vector import Vector
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
     
    x = [ponit[0] for ponit in points]
    y = [ponit[1] for ponit in points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)

    # 沿着X轴进行翻转
    # T = Matrix([[1, 0], [0, -1]])

    # 沿着Y轴进行翻转
    # T = Matrix([[-1, 0], [0, 1]])

    # 关于原点翻转
    # T = Matrix([[-1, 0], [0, -1]])

    # 向右错切
    # T =  Matrix([[1, 0.5], [0, 1]])

    # 向上错切
    # T = Matrix([[1, 0], [0.5, 1]])

    # X扩大2倍，Y扩大1.5倍
    # T = Matrix([[2, 0], [0, 1.5]])

    # 旋转60度
    theta = math.pi / 3
    
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P2 = T.dot(P.T())
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())], 
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()

    



