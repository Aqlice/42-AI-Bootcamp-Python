import sys
sys.path.append('../ex01')
from ImageProcessor import ImageProcessor as imp
import numpy as np

class ColorFilter:
    pass

    def invert(array):
        return 1 - array
    
    def to_blue(array):
        temp= np.zeros(array.shape)
        temp[..., 2] = array[..., 2]
        return temp

    def to_green(array):
        return array * [0, 1, 0]

    def to_red(array):
        temp = array - (ColorFilter.to_blue(array) + ColorFilter.to_green(array))
        return temp

    def to_celluloid(array):
        temp = np.arange(0.0, 1.1, 0.1)
        for i, dim_zero in enumerate(array):
            for j, dim_one in enumerate(dim_zero):
                for k, dim_two in enumerate(dim_one):
                        array[i][j][k] = temp[int(array[i][j][k] * 10)]
        print(array)
        return array

    def to_grayscale(array, filter='weighted'):
        if filter == 'mean':
            mean = np.sum(array, axis=2)/3
            mean = np.broadcast_to(mean[..., None], array.shape)
            return mean
        elif filter == 'weighted':
            weighted = np.sum(array * [0.299, 0.587, 0.114], axis=2)
            weighted = np.tile(weighted[..., None], 3)
            return weighted