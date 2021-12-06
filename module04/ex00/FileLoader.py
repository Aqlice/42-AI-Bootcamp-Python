import pandas as pd

class FileLoader:
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

if __name__ == "__main__":
    data = FileLoader.load('athlete_events.csv')
    FileLoader.display(data, -10)