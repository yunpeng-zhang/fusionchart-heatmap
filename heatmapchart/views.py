from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .static.heatmapchart.fusioncharts import FusionCharts
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

    # dataSource["rows"] = {
    #     "row": [{
    #         "id": "IPHONES5",
    #         "label": "Apple iPhone 5S"
    #     }, {
    #         "id": "SGS5",
    #         "label": "Samsung Galaxy S5"
    #     }, {
    #         "id": "HTC1M8",
    #         "label": "HTC One (M8)"
    #     }, {
    #         "id": "LUMIA",
    #         "label": "Nokia Lumia 1520"
    #     }]
    # }
    # dataSource["columns"] = {
    #     "column": [{
    #         "id": "price",
    #         "label": "Price"
    #     }, {
    #         "id": "processor",
    #         "label": "Processor"
    #     }, {
    #         "id": "screen",
    #         "label": "Screen Size"
    #     }, {
    #         "id": "backup",
    #         "label": "Battery Backup"
    #     }, {
    #         "id": "cam",
    #         "label": "Camera"
    #     }]
    # }
    # dataSource["dataset"] = [{
    #     "data": [{
    #         "rowid": "IPHONES5",
    #         "columnid": "processor",
    #         "value": "-0.8",
    #         "tlLabel": "Dual Core",
    #         "trLabel": "OS : iOS 7"
    #     }, {
    #         "rowid": "IPHONES5",
    #         "columnid": "screen",
    #         "value": "-0.7",
    #         "tlLabel": "4 inch",
    #         "trLabel": "Retina LCD screen"
    #     }, {
    #         "rowid": "IPHONES5",
    #         "columnid": "price",
    #         "value": "-0.5",
    #         "tlLabel": "$649"
    #     }, {
    #         "rowid": "IPHONES5",
    #         "columnid": "backup",
    #         "value": "-0.3",
    #         "tlLabel": "10 Hrs",
    #         "trLabel": "Battery : 1560 MAH"
    #     }, {
    #         "rowid": "IPHONES5",
    #         "columnid": "cam",
    #         "value": "0.1",
    #         "tlLabel": "8 MP",
    #         "trLabel": "Front Camera : 1.2 MP"
    #     }, {
    #         "rowid": "HTC1M8",
    #         "columnid": "processor",
    #         "value": "0.35",
    #         "tlLabel": "Quad Core 2.3 GHz",
    #         "trLabel": "OS : Android 4.4 Kitkat"
    #     }, {
    #         "rowid": "HTC1M8",
    #         "columnid": "screen",
    #         "value": "0.5",
    #         "tlLabel": "5 inch",
    #         "trLabel": "LCD screen"
    #     }, {
    #         "rowid": "HTC1M8",
    #         "columnid": "price",
    #         "value": "0.7",
    #         "tlLabel": "$600"
    #     }, {
    #         "rowid": "HTC1M8",
    #         "columnid": "backup",
    #         "value": "0.9",
    #         "tlLabel": "20 Hrs",
    #         "trLabel": "Battery : 2600 MAH"
    #     }, {
    #         "rowid": "HTC1M8",
    #         "columnid": "cam",
    #         "value": "-0.65",
    #         "tlLabel": "4 MP",
    #         "trLabel": "Front Camera : 5 MP"
    #     }, {
    #         "rowid": "LUMIA",
    #         "columnid": "processor",
    #         "value": "0.95",
    #         "tlLabel": "Quad Core 2.2 GHz",
    #         "trLabel": "OS: Windows Phone 8"
    #     }, {
    #         "rowid": "LUMIA",
    #         "columnid": "screen",
    #         "value": "-0.95",
    #         "tlLabel": "6 inch",
    #         "trLabel": "LCD screen"
    #     }, {
    #         "rowid": "LUMIA",
    #         "columnid": "price",
    #         "value": "0.7",
    #         "tlLabel": "$470"
    #     }, {
    #         "rowid": "LUMIA",
    #         "columnid": "backup",
    #         "value": "0.2",
    #         "tlLabel": "27 Hrs",
    #         "trLabel": "Battery : 3400 MAH"
    #     }, {
    #         "rowid": "LUMIA",
    #         "columnid": "cam",
    #         "value": "0.1",
    #         "tlLabel": "20MP",
    #         "trLabel": "Front Camera : 1.2 MP"
    #     }, {
    #         "rowid": "SGS5",
    #         "columnid": "processor",
    #         "value": "0.7",
    #         "tlLabel": "Quad Core 2.5 GHz",
    #         "trLabel": "OS : Android 4.4 Kitkat"
    #     }, {
    #         "rowid": "SGS5",
    #         "columnid": "screen",
    #         "value": "0.5",
    #         "tlLabel": "5.1 inch",
    #         "trLabel": "AMOLED screen"
    #     }, {
    #         "rowid": "SGS5",
    #         "columnid": "price",
    #         "value": "0.3",
    #         "tlLabel": "$600"
    #     }, {
    #         "rowid": "SGS5",
    #         "columnid": "backup",
    #         "value": "0.45",
    #         "tlLabel": "29 Hrs",
    #         "trLabel": "Battery : 2800 MAH"
    #     }, {
    #         "rowid": "SGS5",
    #         "columnid": "cam",
    #         "value": "0.6",
    #         "tlLabel": "16 MP",
    #         "trLabel": "Front Camera : 2.1 MP"
    #     }]
    # }]
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
