import pandas as pd
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
import matplotlib
>>>>>>> e96fefe25ae6e8f5a05e237cb09b4ff8fe2f313b

data = pd.read_csv("example_file.txt",
                    sep = " ",
                    names = ["time","tempature", "humidity", "light", "rain"], 
                    index_col="time"
                    )

<<<<<<< HEAD
xpoints = data.index
ypoints = data["tempature"]

plt.plot(xpoints, ypoints)
plt.show()

#I sadly dont have that much time to programm because of school 
=======
data = pd.read_csv("example_file.txt", sep = " ", names = ["tempature", "humidity", "light", "rain", "time"], index_col="time")
>>>>>>> e96fefe25ae6e8f5a05e237cb09b4ff8fe2f313b
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with



