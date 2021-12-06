import pandas as pd

class FileLoader:
    @staticmethod
    def load(path):
        data = pd.read_csv(path)
        newdata = pd.DataFrame(data)
        print(f'Loading dataset of dimensions {newdata.shape[0]}'
              f' x {newdata.shape[1]}')
        return newdata

    def display(data, n):
        if n > 0:
            print(data[:n])
        else:
            print(data[:n - 1:-1])