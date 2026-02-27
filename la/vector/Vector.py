class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding, Length of vectors must be same"
        
        return Vector([a + b for a, b in zip(self, another)])
    
    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in sub, Length of vectors must be same"
        
        return Vector([a - b for a, b in zip(self, another)])
    
    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""
        return Vector([k * x for x in self])
    
    def __rmul__(self, k):
         """返回数量乘法的结果向量：k * self"""
         return self * k

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self
    
    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __iter__(self):
        """返回向量迭代器"""
        return self._values.__iter__()
    
    def __repr__(self):
        return "Vector({})".format(self._values)
    
    def __str__(self):
        """print方法调用时会调用该方法"""
        return "({})".format(",".join(str(x) for x in self._values))