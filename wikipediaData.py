import pandas as pd
import geopandas as gpd
import folium

# get dataset of meatconsumption by country from wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'
tables = pd.read_html(url)
table = tables[0]


# set dataframe parameters for table
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 200)

# get world gis data from geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# join-left sql command on merging datasets to prep map data
table = world.merge(table, how='left', left_on=['name'], right_on=['Country'])
table = table.dropna(subset=['kg/person (2002)[9][note 1]'])
print(table)

# load a folium map
my_map = folium.Map()
folium.Choropleth(
    geo_data=table,
    name='chloropleth',
    data=table,
    columns=['Country', 'kg/person (2002)[9][note 1]'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.7,
    legend_name='Meat consumption in kg/person'
).add_to(my_map)

# create an html file from the reults
my_map.save('meat.html')