import plotly.express as px
import csv
with open("csv files\Student Marks vs Days Present.csv",encoding = "utf-8") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Marks In Percentage",y = "Days Present")
    fig.show()