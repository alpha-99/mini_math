from vector.Vector import Vector
from matrix.Matrix import Matrix

"""
    线性代数的系统视角，其实是一组n元一次方程组，他可以看做是矩阵。

    求解方式：
        Gauss elimination
        Gauss-Jordan elimination
"""
class LinearSystem:
    """
    A: 系数矩阵
    b: 结果向量
    """
    def __init__(self, A, b):
        assert A.row_num() == len(b), "row number of A must be equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n # TODO: no this restriction

        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]

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
        n = self._m
        for i in range(n):
            # Ab[i][i]为主元
            max_row = self._max_row(i, i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            # 主元归一
            self.Ab[i] = self.Ab[i] / self.Ab[i][i] # TODO: self.Ab[i][i] == 0?
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            # Ab[i][i]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()


    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])