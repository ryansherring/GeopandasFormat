### Geopandas Formatting ###

The goal of this short script is to take tabular data and digest the data into an HTML formatted map.

First, we pull data from wikipedia, namely because they provide `table` html elements and have numerous 'data x' by country pages to fraw from, so that we can make a world map.

Next, we use pandas to make a dataframe and prep the data and make a map object from geopandas. We then finish prepping the data with sql queries
