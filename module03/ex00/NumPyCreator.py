import numpy as np

class NumPyCreator:
    pass

    @staticmethod
    def from_list(lst):
        return np.asarray(lst)
    
    @staticmethod
    def from_tuple(lst):
        return np.asarray(lst)

    @staticmethod
    def from_iterable(iter):
        return np.fromiter(iter, float)

    @staticmethod
    def from_shape(shape, value=0):
        return np.full(shape, value)

    @staticmethod
    def random(shape):
        return np.random.random(shape)

    @staticmethod
    def identity(n):
        return np.eye(n)