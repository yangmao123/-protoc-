import requests
import struct

data = requests.get("https://services5.arcgis.com/7nsPwEMP38bSkCjy/ArcGIS/rest/services/LA_Pre_outbreak_mobility_data/FeatureServer/0/query?f=pbf&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=ObjectId%20ASC&outSR=102100&resultOffset=0&resultRecordCount=30442&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22edit%22%7D")
print(data.content)

with open("data.bin", "ab+") as f:
    f.write(data.content)
