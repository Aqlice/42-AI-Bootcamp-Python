import pandas as np
from FileLoader import FileLoader

def ProportionBySport(data, year, sport, sex):
    newdata = data[(data['Year']==year) & (data['Sex']==sex)]
    newdata = newdata.drop_duplicates(subset='Name')
    res = newdata[newdata['Sport']==sport]
    return float(res.shape[0] / newdata.shape[0])

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    print(ProportionBySport(data, 2004, 'Tennis', 'F'))
