import plotly.express as px
import csv
with open("csv files\cups of coffee vs hours of sleep.csv",encoding = "utf-8") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Coffee in ml",y = "sleep in hours")
    fig.show()