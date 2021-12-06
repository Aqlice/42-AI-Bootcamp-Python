import pandas as pd
from FileLoader import FileLoader

def youngestFellah(data, year):
    newdata = data[data['Year']==year]
    newdata = newdata.sort_values(by=['Age'])
    first = newdata.iloc[0]
    i = 1
    while newdata.iloc[i]['Sex'] == first['Sex']:
        i += 1
    opposite = newdata.iloc[i]
    return {first['Sex']: first['Age'], opposite['Sex']: opposite['Age']}

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    print(youngestFellah(data, 1996))