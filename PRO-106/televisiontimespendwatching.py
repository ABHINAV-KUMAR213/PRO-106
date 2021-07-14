import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    average_time_spend= []
    with open(data_path,encoding = "utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spend.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return{"x":size_of_tv,"y":average_time_spend}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation between size of tv anaverage time spend watching tv : \n - - -",corelation[0,1])

def setup():
    data_path = "csv files\Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)
setup()

