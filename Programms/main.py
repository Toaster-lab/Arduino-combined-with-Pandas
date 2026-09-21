import pandas as pd
import numpy as np
import matplotlib


data = pd.read_csv("example_file.txt", sep = " ", names = ["tempature", "humidity", "light", "rain"], index_col="Time")
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with

