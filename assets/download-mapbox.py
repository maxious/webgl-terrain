import requests
import json
import urllib
import os

#https://www.mapbox.com/developers/api/static/
#http://wiki.openstreetmap.org/wiki/Zoom_levels
#http://stackoverflow.com/a/10970121/684978
access_token = ""
center_lat = -35.5
center_lon = 148.5
scale = 0.352 # zoom 10, degrees per 256 pixels
url = "http://api.tiles.mapbox.com/v4/examples.map-zr0njcqy/148.5,-35.5,10/1280x1280.png?access_token="

center_lat = -34.5
center_lon = 149.49
scale = 0.703 # zoom 10, degrees per 256 pixels
#url = "http://api.tiles.mapbox.com/v4/examples.map-zr0njcqy/149.4998611,-34.5001389,9/1280x1280.png?access_token="
url = "http://api.tiles.mapbox.com/v4/maxious.jm8lch50/149.4998611,-34.5001389,9/1280x1280.png?access_token="

filename = str(center_lon)+str(center_lat)
if not os.path.isfile(filename+'.png'):
	urllib.urlretrieve(url,filename+'.png')
#1280/2 = 640
#-gcp [pixelX lineY eastingX northingY]
center = "640 640 " + str(center_lon) + " " +str(center_lat)
center_top = "640 0 "+ str(center_lon) + " " + str(center_lat + scale * 2)
top_left = "0 0 " + str(center_lon - scale * 2.5) + " " +str(center_lat + scale * 2)

print ("gdal_translate -of GTiff -a_srs EPSG:4326 -gcp %s -gcp %s -gcp %s %s %s"  % (center,top_left,center_top,filename+'.png',filename+'.tiff'))
print ("gdalwarp %s %s"  % (filename+'.tiff',filename+'-gps.tiff'))
print 'gdal_translate -projwin 147.9998611 -33.0001389 150.9998611 -36.0001389 -of png 149.49-34.5-gps.tiff canberra-texture.png'
