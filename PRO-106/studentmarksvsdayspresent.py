import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks_and_percentage = []
    days_present= []
    with open(data_path,encoding = "utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_and_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x":marks_and_percentage,"y":days_present}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation between percentage of marks and days present : \n - - -",corelation[0,1])

def setup():
    data_path = "csv files\Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)
setup()

