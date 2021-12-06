import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader
import  seaborn as sns

class Komparator:
    def __init__(self, data):
        self.dataset = data

    def compare_box_plots(self, categorical_var, numerical_var):
        nb = self.dataset[categorical_var].drop_duplicates()
        fig, axis = plt.subplots(ncols=len(nb))
        my_list = []
        for elem in nb:
            my_list.append(elem)
        for i in range(len(my_list)):
            sns.boxplot(self.dataset[numerical_var][self.dataset[categorical_var]==my_list[i]],ax=axis[i])
            axis[i].set_title(my_list[i])
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        nb = self.dataset[categorical_var].drop_duplicates()
        fig, axis = plt.subplots(ncols=len(nb))
        my_list = []
        for elem in nb:
            my_list.append(elem)
        for i in range(len(my_list)):
            axis[i].hist(self.dataset[numerical_var][self.dataset[categorical_var]==my_list[i]])
            axis[i].set_title(my_list[i])
        plt.show()
    
    def density(self, categorical_var, numerical_var):
        nb = self.dataset[categorical_var].drop_duplicates()
        my_list = []
        for elem in nb:
            my_list.append(elem)
        for i in range(len(my_list)):
            sns.kdeplot(self.dataset[numerical_var][self.dataset[categorical_var]==my_list[i]], label=f'means {my_list[i]}')
            plt.legend()
            plt.title(f'Density for {categorical_var}')
        plt.show()

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ressources/athlete_events.csv')
    kpr = Komparator(data)
    kpr.density("Sex", "Height")
    kpr.compare_histograms("Sex", "Height")
    kpr.compare_box_plots("Sex", "Height")
