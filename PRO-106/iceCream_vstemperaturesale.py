import plotly.express as px
import csv
with open("csv files\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv",encoding = "utf-8") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Temperature",y = "Ice-cream Sales( ₹ )")
    fig.show()