import plotly.express as px
import csv
import numpy as np


with open("SizeOfTvVsTimeSpent.csv") as file:
    dataFrame = csv.DictReader(file)

    figure = px.scatter(dataFrame, x="Size of TV",
                        y="Average time spent watching TV in a week (hours)")
    figure.show()


def getDataSource():
    source = 'SizeOfTvvsTimeSpent.csv'
    size = []
    time = []

    with open(source) as file:
        csvreader = csv.DictReader(file)

        for x in csvreader:
            size.append(float(x["Size of TV"]))
            time.append(
                float(x["Average time spent watching TV in a week (hours)"]))

    return {'x': size, 'y': time}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])


def setup():
    dataSource = getDataSource()
    findCorrelation(dataSource)


setup()
