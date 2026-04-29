from matrix.Matrix import Matrix
from linearsystem.LinearSystem import rank

def gram_schmidt_process(basis):

    matrix = Matrix(basis)

    assert rank(matrix) == len(basis), "Error in Gram-Schmidt Process. The basis is not linearly independent."

    # res存放的是已经正交的向量，初始时第一个向量不变
    res = [basis[0]]
    """对每个向量进行正交化处理"""
    for i in range(1, len(basis)):
        p = basis[i]
        for r in res:
            p = p - basis[i].dot(r) / r.dot(r) * r

        res.append(p)

    return res       

# QR分解
def qr(A):
    assert A.row_num() == A.col_num(), "A must be a square matrix."

    bisis = [A.col_vector(i) for i in range(A.col_num())]

    # 正交基矩阵
    P = gram_schmidt_process(basis=bisis)

    # 标准正交矩阵, Q的逆等于Q的转置
    Q = Matrix([v/v.norm() for v in P]).T()

    # 计算R矩阵， R = Q^T * A
    R = Q.T().dot(A)

    return Q, R

