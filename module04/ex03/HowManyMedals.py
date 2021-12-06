import pandas as np
from FileLoader import FileLoader

def howmanymedals(data, name):
    data = data[data['Name']==name]
    my_dict = {}
    for index, row in data.iterrows():
        year = row['Year']
        medal = row['Medal']
        if year not in my_dict.keys():
            my_dict.update({year:{'G': 0, 'S': 0, 'B': 0}})
        if medal == 'Gold':
            my_dict[year]['G'] += 1
        if medal == 'Silver':
            my_dict[year]['S'] += 1
        if medal == 'Bronze':
            my_dict[year]['B'] += 1
    return my_dict


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    print(howmanymedals(data, "Kjetil Andr Aamodt"))