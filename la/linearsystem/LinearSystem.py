from vector.Vector import Vector
from matrix.Matrix import Matrix
from vector._globals import is_zero

"""
    线性代数的系统视角，其实是一组n元一次方程组，他可以看做是矩阵。

    求解方式：
        Gauss elimination
        Gauss-Jordan elimination
"""
class LinearSystem:
    """
    A: 系数矩阵
    b: 结果向量或结果矩阵
    """
    def __init__(self, A, b):
        assert A.row_num() == len(b), "row number of A must be equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        # assert self._m == self._n # TODO: no this restriction，一般的gauss jordan不一定m和n相等

        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]
        
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]

        self.pivots = [] # pivots用于存储主元的列

    def _max_row(self, index_i, index_j, n):
        """
            查找当前主元下面的行中第一个元素最大的行
            返回最大的元素所在的行
        """
        best, ret = abs(self.Ab[index_i][index_j]), index_i
        for i in range(index_i + 1, n):
            if abs(self.Ab[i][index_j]) > best:
                best, ret = self.Ab[i][index_j], i

        return ret

    def _forward(self):
        
        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][k]位置是否可以为主元
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 主元归一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        """
            主元的个数其实也是行数，pivot里面存储的是主元的个数，
            所以在向后消元过程中从主元个数的行开始
        """
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            # Ab[i][k]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):
        """如果有解，返回True，如果没有解，返回False"""
        self._forward()
        self._backward()

        for i in range(len(self.pivots), self._m):
            # 系数全为0，结果向量不为0
            if is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])

def inv(A):
    """求解矩阵的逆，A为方阵"""
    if A.row_num() != A.col_num():
        return None
    
    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None
    
    invA = [[row[i] for i in range(n, 2 * n)] for row in ls.Ab]
    return Matrix(invA)       