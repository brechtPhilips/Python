import pygal
import pandas



data = pandas.read_csv("Files/countries_big_area.csv")


def CreatePieChart(data):
    pieChart = pygal.Pie()
    pieChart.title = 'PieChart'
    for index,row in data.iterrows():
        pieChart.add(row["Country"],int(row["Population"]))

    pieChart.render_to_file('Files/pieChart.svg')

def CreateBarChart(data):
    barChart = pygal.HorizontalBar(style=NeonStyle)
    barChart.titile = 'Population per Country Bar'
    for index,row in data.iterrows():
        barChart.add(row["Country"],int(row["Population"]))

    barChart.render_to_file('Files/barChart.svg')
def CreateTreeMap(data):
    treemap = pygal.Treemap()
    treemap.titile = 'Population per Country Treemap'
    for index,row in data.iterrows():
        treemap.add(row["Country"],int(row["Population"]))

    treemap.render_to_file('Files/treeMap.svg')

CreatePieChart(data)
CreateBarChart(data)
CreateTreeMap(data)