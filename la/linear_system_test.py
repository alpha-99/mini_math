from vector.Vector import Vector
from matrix.Matrix import Matrix
from linearsystem.LinearSystem import LinearSystem
from linearsystem.LinearSystem import inv, rank

if __name__ == "__main__":

    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
    print()

    A2 = Matrix([[1, -3, 5], [2, -1, -3], [3, 1, 4]])
    b2 = Vector([-9, 19, -13])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print()

    A3 = Matrix([[1, 2, -2], [2, -3, 1], [3, -1, 3]])
    b3 = Vector([6, -10, -16])
    ls3 = LinearSystem(A3, b3)
    ls3.gauss_jordan_elimination()
    ls3.fancy_print()
    print()

    A4 = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    b4 = Vector([4, 32, 13])
    ls4 = LinearSystem(A4, b4)
    ls4.gauss_jordan_elimination()
    ls4.fancy_print()
    print()

    A5 = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    b5 = Vector([31, 36, 11])
    ls5 = LinearSystem(A5, b5)
    ls5.gauss_jordan_elimination()
    ls5.fancy_print()
    print()

    A6 = Matrix([[1, 1, 1], [1, -1, -1], [2, 1, 5]])
    b6 = Vector([3, -1, 8])
    ls6 = LinearSystem(A6, b6)
    ls6.gauss_jordan_elimination()

    print("A6")
    ls6.fancy_print()
    print()

    A7 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b7 = Vector([1, 5, 13, -1])
    ls7 = LinearSystem(A7, b7)
    ls7.gauss_jordan_elimination()

    print("A7")
    ls7.fancy_print()
    print()

    A8 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]])
    b8 = Vector([3, 2.5, 7])
    ls8 = LinearSystem(A8, b8)
    if not ls8.gauss_jordan_elimination():
        print("No Solution!")
    
    print("A8")
    ls8.fancy_print()
    print()

    A9 = Matrix([[2, 0, 1],
                 [-1, -1, -2],
                 [-3, 0, 1]])
    b9 = Vector([1, 0, 0])
    ls9 = LinearSystem(A9, b9)
    if not ls9.gauss_jordan_elimination():
        print("No Solution!")
    
    print("A9")
    ls9.fancy_print()
    print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    print(A.dot(invA))
    print(invA.dot(A))

    print("rank A8 = {}".format(rank(A8))) # 2
    print("rank A7 = {}".format(rank(A7))) # 3
    print("rank A6 = {}".format(rank(A6))) # 3