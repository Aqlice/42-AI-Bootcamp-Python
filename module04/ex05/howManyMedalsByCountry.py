import pandas as pd
from FileLoader import FileLoader

def howManyMedalsByCountry(data, team):
    data = data[data['Team']==team]
    data = data[(data['Medal']=='Gold') | (data['Medal']=='Silver') | (data['Medal']=='Bronze')]
    data = data[['Year', 'Event', 'Medal']].drop_duplicates()
    data = data.sort_values(by='Year')
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

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load('../ressources/athlete_events.csv')
    std = howManyMedalsByCountry(data, 'Portugal')
    print(std)