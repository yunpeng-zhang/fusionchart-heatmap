from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .static.fusioncharts.fusioncharts import FusionCharts
import pandas as pd
import json


def myFirstChart(request):
    # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Crypto Correlation Heatmap"
    chartConfig["subCaption"] = ""
    chartConfig["xAxisName"] = "Ticker"
    chartConfig["yAxisName"] = "Ticker"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"
    chartConfig["showValues"] = "1"
    chartConfig["showPlotBorder"] = "1"
    chartConfig["xAxisPosition"] = "top"
    chartConfig["xAxisValueFontSize"] = "20"
    chartConfig["yAxisValueFontSize"] = "20"    

    dataSource["chart"] = json.dumps(chartConfig)
    # print(dataSource["chart"])
    # read in data->pd->json
    df = pd.read_csv("crypto_corr.csv", index_col="Ticker")
    df_header = list(df.columns.values)
    # print(df_header)
    # dataSource = OrderedDict()
    # create row data
    row = []
    for item in df_header:
        row.append({"id": item, "label": item})
    rows = {"row": row}
    dataSource["rows"] = rows
    # print(dataSource["rows"])
    # create column data 
    column = row
    columns = {"column": column}
    dataSource["columns"] = columns
    # print(dataSource["columns"])
    # create dataset
    table = []
    for i in range(len(df_header)):
        for j in range(len(df_header)):
            table.append(
                {"rowid": df_header[i], "columnid": df_header[j], "value": df.iloc[i, j]})
    tables = {"data": table} 
    dataSource["dataset"] = [tables] # no need to use json.dumps as fusioncharts will prepare the data as json ready
    # print(dataSource["dataset"])
   
    dataSource["colorRange"] = {
        "gradient": "0.1",
        "minValue": "-1.00",
        "code": "#e24b1a",
        "startLabel": "Negative",
        "endLabel": "Positive",
        "color": [{
            "code": "#e24b1a",
            "minValue": "-1",
            "maxValue": "-0.5",
                "label": ""
                }, {
            "code": "#f6bc33",
            "minValue": "-0.5",
                "maxValue": "0",
                "label": ""
                }, {
            "code": "#319413",
            "minValue": "0",
                "maxValue": "0.5",
                "label": ""
                }, {
            "code": "#014d06",
            "minValue": "0.5",
                "maxValue": "1",
                "label": ""
                }]
    }

    # Create an object for the heatmap 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    heatmap2D = FusionCharts("heatmap", "myFirstChart",
                            "900", "400", "myChartHeatmap", "json", dataSource)
    return render(request, 'index.html', {'output': heatmap2D.render()})
