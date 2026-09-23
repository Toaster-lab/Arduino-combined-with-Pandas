import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("example_file.txt",
                    sep = " ",
                    names = ["time","tempature", "humidity", "light", "rain"], 
                    index_col="time"
                    )

xpoints = data.index
ypoints = data["tempature"]

plt.plot(xpoints, ypoints)
plt.show()

#I sadly dont have that much time to programm because of school 
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with