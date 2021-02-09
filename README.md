### Geopandas Formatting ###

The goal of this short script is to take tabular data and digest the data into an HTML formatted map.

First, we pull data from wikipedia, namely because they provide `table` html elements and have numerous 'data x' by country pages to fraw from, so that we can make a world map.

Next, we use pandas to make a dataframe and prep the data and make a map object from geopandas. Luckily, shapely provides geometry to make a geodataframe through geopandas. We wrap up printing a leaflet map using folium.

It's a very simple script, but it's good for showing how simple it can be to transform tables to geometric objects.
