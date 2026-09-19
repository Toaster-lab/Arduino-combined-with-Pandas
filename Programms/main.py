import pandas as pd
import numpy as np


data = pd.read_csv("example_file.txt", sep = " ", names = ["tempature", "humidity", "light", "rain"])
#this is an example, the order of information is not fixed yet
#this is gonna give me data set to work with