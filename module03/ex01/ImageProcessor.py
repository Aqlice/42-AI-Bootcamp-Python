import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:
    pass

    @staticmethod
    def load(path):
        img = mpimg.imread(path)
        print(f'Loading image of dimensions {img.shape[0]} x {img.shape[1]}, dtype : {img.dtype}')
        return(img)

    @staticmethod
    def display(array, axis='on'):
        if axis == 'off':
            plt.axis('off')
        plt.imshow(array)
        plt.show()