import numpy as np
import sys
sys.path.append('../ex01')
sys.path.append('../ex00')
from NumPyCreator import NumPyCreator as nmp
from ImageProcessor import ImageProcessor

class ScrapBooker:
    pass

    @staticmethod
    def crop(array, dimensions, position=(0,0)):
        if dimensions[0] > array.shape[0] or \
           dimensions[1] > array.shape[1]:
            sys.exit("Error, dimensions superior to image")    
        cr = array[position[0]:position[0] + dimensions[0], 
             position[1]:position[1] + dimensions[1]]
        return cr
    
    @staticmethod
    def thin(array, n, axis):
        axis = int(not axis)
        return np.delete(array, slice(n -1, None, n), axis)
    
    @staticmethod
    def juxtapose(array, n, axis):
        copy = np.copy(array)
        for x in range(n):
            copy = np.concatenate((copy, array), axis)
        return copy

    def mosaic(self, array, dimensions):
        mosaic = self.juxtapose(array, dimensions[0] -1, 0)
        mosaic = self.juxtapose(mosaic, dimensions[1] -1, 1)
        return mosaic