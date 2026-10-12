import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "Programms/temperature.txt",
    sep=r"\s+",
    names=["humidity", "temperature", "light", "rain", "date", "time"]
)

font = plt.xticks(fontsize=8, rotation=45)

data = data.set_index("time")
data = data.sort_index()

#converting no rain and rain to binary
data["rain1_0"] = np.where(data["rain"] == 1023, 0, 1)

#min,max,mean
min_temperature = data["temperature"].min()
max_temperature = data["temperature"].max()
mean_temperature = data["temperature"].mean()

daily_summary = data.groupby("date").agg({
    "temperature": ["min", "max", "mean"],
    "humidity": "mean",
    "rain1_0": "sum"
})
xpoints = data.index


class CreatingDiagram:
    def __init__(self, shown_data: str) -> None:
        self.shown_data = shown_data

    def show_diagram(self) -> None:
        plt.plot(xpoints, data[self.shown_data])
        plt.xlabel("Timestamp")
        plt.ylabel(f"Showing {self.shown_data}")
        font
        plt.tight_layout()
        plt.show()


class WeatherAnalysis:
    def __init__(self, data) -> None:
        self.data = data

    def show_temperature_stats(self) -> None:
        print("Minimum: ", min_temperature)
        print("Maximum: ", max_temperature)
        print("Average: ", mean_temperature)

    def show_daily_summary(self) -> None:
        print(daily_summary)

    def show_rain(self) -> None:
        plt.step(self.data.index, self.data["rain1_0"], where="mid")
        plt.xlabel("Time")
        plt.ylabel("Rain in binary")
        plt.yticks([0, 1]) #only two available values
        font
        plt.tight_layout()
        plt.show()

weather = WeatherAnalysis(data)
weather.show_temperature_stats()
weather.show_daily_summary()
weather.show_rain()

temperature_diagram = CreatingDiagram("temperature")
temperature_diagram.show_diagram()
#I sadly dont have that much time to programm because of school 
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with