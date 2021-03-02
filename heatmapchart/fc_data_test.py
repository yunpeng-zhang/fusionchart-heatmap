from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
import pandas as pd
import json
# Include the `fusioncharts.py` file that contains functions to embed the charts.

# from .static.heatmapchart.fusioncharts import FusionCharts

# dataSource=OrderedDict() # list of dictionaries
# dataSource["data"] = []
# # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
# # Insert the data into the `dataSource['data']` list.
# dataSource["data"].append({"label": 'Venezuela', "value": '290'})
# dataSource["data"].append({"label": 'Saudi', "value": '290'})
# dataSource["data"].append({"label": 'Canada', "value": '180'})
# dataSource["data"].append({"label": 'Iran', "value": '140'})
# dataSource["data"].append({"label": 'Russia', "value": '115'})
# dataSource["data"].append({"label": 'Russia', "value": '115'})
# dataSource["data"].append({"label": 'UAE', "value": '100'})
# dataSource["data"].append({"label": 'US', "value": '30'})
# dataSource["data"].append({"label": 'China', "value": '30'})
# print(dataSource["data"])
# # Output: [{'label': 'Venezuela', 'value': '290'}, {'label': 'Saudi', 'value': '290'}, {'label': 'Canada', 'value': '180'}, {'label': 'Iran', 'value': '140'}, {'label': 'Russia', 'value': '115'}, {'label': 'Russia', 'value': '115'}, {'label': 'UAE', 'value': '100'}, {'label': 'US', 'value': '30'}, {'label': 'China', 'value': '30'}]

df=pd.read_csv("crypto_corr.csv", index_col="Ticker")
df_header=list(df.columns.values)
print(df_header)

dataSource = OrderedDict()
# create row data
row=[]
for item in df_header:
    row.append({"id": item, "label": item})
rows = {"row": row}
dataSource["rows"] = json.dumps(rows)
print(dataSource["rows"])
# create column data
column = row
columns ={"column": column}
dataSource["columns"] = json.dumps(columns)
print(dataSource["columns"])
# create dataset
table=[]
for i in range(len(df_header)):
    for j in range(len(df_header)):
        table.append({"rowid": df_header[i], "columnid": df_header[j], "value": df.iloc[i, j]})
tables = []
tables.append({"data": table})
dataSource["dataset"] = json.dumps(tables)
print(dataSource["dataset"])


