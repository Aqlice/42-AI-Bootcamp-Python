import pandas as np
from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
    
    def when(self, location):
        self.data = self.data[self.data['City']==location]
        return self.data['Year'].drop_duplicates().tolist()

    def where(self, year):
        self.data = self.data[self.data['Year']==year]
        return self.data.iloc[0]['City']






if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ressources/athlete_events.csv')
    std = SpatioTemporalData(data)
    print(std.where(2016))