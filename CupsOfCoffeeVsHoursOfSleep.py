import plotly.express as px
import csv
import numpy as np


with open("CoffeeIntakeVsSleep.csv") as file:
    dataFrame = csv.DictReader(file)

    figure = px.scatter(dataFrame, x="Coffee in ml", y="sleep in hours")
    # figure.show()


def getDataSource():
    source = 'CoffeeIntakeVsSleep.csv'
    coffee = []
    sleep = []

    with open(source) as file:
        csvreader = csv.DictReader(file)

        for x in csvreader:
            print(x)
            coffee.append(float(x["Coffee in ml"]))
            sleep.append(float(x["sleep in hours"]))

    return {'x': coffee, 'y': sleep}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])


def setup():
    dataSource = getDataSource()
    findCorrelation(dataSource)


setup()
