from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    def histogram(data, features):
        data[features].hist()
        plt.show()

    def density(data, features):
        data[features].plot.kde()
        plt.show()

    def pair_plot(data, features):
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    def box_plot(data, features):
        data[features].plot.box()
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ressources/athlete_events.csv')
    mpl = MyPlotLib

    mpl.histogram(data, ["Height", "Weight"])
    mpl.density(data, ["Weight", "Height"])
    mpl.pair_plot(data, ["Weight", "Height"])
    mpl.box_plot(data, ["Weight", "Height"])