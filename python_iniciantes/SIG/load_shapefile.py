import geopandas as gpd
import matplotlib.pyplot as plt 


gpd = gpd.read_file('lhas.shp')
gpd =gpd.to_crs(epsg=4326)

print(gpd.head())
gpd.plot()