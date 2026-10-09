import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "Programms/temperature.txt",
    sep=r"\s+",
    names=["humidity", "temperature", "light", "rain","date","time"],
    index_col="time"
)

xpoints = data.index

class CreatingDiagram:
    def __init__(self, shown_data : str) -> None:
        self.shown_data = shown_data
    def show_diagram(self) -> None:
        plt.plot(xpoints, data[self.shown_data])
        plt.xlabel("Timestamp")
        plt.ylabel(f"Showing {self.shown_data}")
        plt.xticks(fontsize=8, rotation = 45)
        plt.show()


temperature_diagram = CreatingDiagram("temperature")
temperature_diagram.show_diagram()
#I sadly dont have that much time to programm because of school 
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with