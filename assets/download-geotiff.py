import requests
import json
import urllib
import os

def getTiles(collection,r):
	for layer in r.json()['catalogItems']['features']:
		print layer['attributes']['Name']
		url = 'http://www.ga.gov.au/gisimg/rest/services/topography/'+collection+'/ImageServer/file?id=*'+str(layer['attributes']['Name'])+'.'+str(layer['attributes']['OBJECTID'])+'%40rasterIds%3D'+str(layer['attributes']['OBJECTID'])
		print url
		if not os.path.isfile(layer['attributes']['Name']+'.tiff'):
			urllib.urlretrieve(url,layer['attributes']['Name']+'.tiff')

for collection in ['dem_1s','dem_s_1s']:
	r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/'+collection+'/ImageServer/identify?geometry=%7B+%22rings%22+%3A+%5B+%5B+%5B148%2C-34%5D%2C%5B150%2C-34%5D%2C%5B150%2C-36%5D%2C%5B148%2C-34%5D+%5D+%5D%2C%22spatialReference%22+%3A+%7B%22wkid%22+%3A+4326%7D+%7D&geometryType=esriGeometryPolygon&mosaicRule=&pixelSize=3%2C3&f=pjson')
	getTiles(collection,r)
	r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/'+collection+'/ImageServer/identify?geometry=148%2C-35.5&geometryType=esriGeometryPoint&mosaicRule=&pixelSize=3%2C3&f=pjson')
	getTiles(collection,r)


#r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/dem_1s/ImageServer/identify?geometry=%7B+%22rings%22+%3A+%5B+%5B+%5B148%2C-34%5D%2C%5B150%2C-34%5D%2C%5B150%2C-36%5D%2C%5B148%2C-34%5D+%5D+%5D%2C%22spatialReference%22+%3A+%7B%22wkid%22+%3A+4326%7D+%7D&geometryType=esriGeometryPolygon&mosaicRule=&pixelSize=3%2C3&f=pjson')
#getTiles('dem_1s',r)
#r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/dem_1s/ImageServer/identify?geometry=148%2C-35.5&geometryType=esriGeometryPoint&mosaicRule=&pixelSize=3%2C3&f=pjson')
#getTiles('dem_1s',r)

#r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/dem_s_1s/ImageServer/identify?geometry=%7B+%22rings%22+%3A+%5B+%5B+%5B148%2C-34%5D%2C%5B150%2C-34%5D%2C%5B150%2C-36%5D%2C%5B148%2C-34%5D+%5D+%5D%2C%22spatialReference%22+%3A+%7B%22wkid%22+%3A+4326%7D+%7D&geometryType=esriGeometryPolygon&mosaicRule=&pixelSize=3%2C3&f=pjson')
#getTiles('dem_s_1s',r)
#r = requests.get('http://www.ga.gov.au/gisimg/rest/services/topography/dem_s_1s/ImageServer/identify?geometry=148%2C-35.5&geometryType=esriGeometryPoint&mosaicRule=&pixelSize=3%2C3&f=pjson')
#getTiles('dem_s_1s',r)
