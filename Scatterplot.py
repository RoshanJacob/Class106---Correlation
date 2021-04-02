import plotly.express as px
import pandas as pd
import numpy as np


with open("SizeOfTvVsTimeSpent.csv") as file:
    dataFrame = pd.read_csv(file)

    figure = px.scatter(dataFrame, x="Size of TV",
                        y="Average time spent watching TV in a week (hours)")
    figure.show()
