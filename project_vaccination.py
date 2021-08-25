##************************************************************************************************
##   Tijana Plakalvic
##   Ontario Vaccination Rate (per age group): includes vaccination rates for age groups 12-17,
##   18-29 and 30-39.
##************************************************************************************************

import csv #imports the data
import geopandas as gpd
import pandas as pd
from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.models import Slider, HoverTool
import json
from bokeh.palettes import brewer
from bokeh.models import CheckboxButtonGroup, RadioButtonGroup, CustomJS
from bokeh.layouts import widgetbox, row, column

covid_map = "ontario_map/Ministry_of_Health_Public_Health_Unit_Boundary.shp" #Same public health divisions

#Open .csv file using dictionaries
input_data = csv.DictReader(open(covid_data))

# Open files using GeoPandas and Pandas
data_map_df = gpd.read_file(covid_map)[['OGF_ID', 'PHU_NAME_E', 'geometry']]
covid_data_df = pd.DataFrame.from_dict(input_data)

# Fetch data for the latest date and merge it to the map
latest_covid_data_df = covid_data_df[covid_data_df['FILE_DATE'] == "20200410"]
merged = data_map_df.merge(latest_covid_data_df, left_on="PHU_NAME_E", right_on="PHU_NAME")

#Read data to json.
merged_json = json.loads(merged.to_json())

#Convert to String like object. 
json_data = json.dumps(merged_json)

#Define function that returns json_data for year selected by user.    
def json_data_mapping(date):
    dt = date
    print(str(dt))
    print(covid_data_df['FILE_DATE'] == str(dt))
    c19df_dt = covid_data_df[covid_data_df['FILE_DATE'] == str(dt)]
    merged = data_map_df.merge(latest_covid_data_df, left_on="PHU_NAME_E", right_on="PHU_NAME")
    #merged.fillna('No data', inplace = True)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data
