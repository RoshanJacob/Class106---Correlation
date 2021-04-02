import plotly.express as px
import csv
import numpy as np


with open("AttendanceVsStudentMarks.csv") as file:
    dataFrame = csv.DictReader(file)

    figure = px.scatter(dataFrame, x="Days Present", y="Marks In Percentage")
    figure.show()


def getDataSource():
    source = 'AttendanceVsStudentMarks.csv'
    daysPresent = []
    marksInPercentage = []

    with open(source) as file:
        csvreader = csv.DictReader(file)

        for x in csvreader:
            daysPresent.append(float(x["Days Present"]))
            marksInPercentage.append(float(x["Marks In Percentage"]))

    return {'x': daysPresent, 'y': marksInPercentage}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])


def setup():
    dataSource = getDataSource()
    findCorrelation(dataSource)


setup()
