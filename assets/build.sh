gdalbuildvrt canberra-1s.vrt e*dem1*
gdalwarp canberra-1s.vrt canberra-1s.tif
gdalinfo -mm canberra-1s.tif
gdal_translate -scale -98 1898 0 255 -outsize 200 200 -of PNG canberra-1s.tif canberra-1s.png
gdal_translate -scale -98 1898 0 65535 -ot UInt16 -outsize 200 200 -of ENVI canberra-1s.tif canberra-1s.bin

gdalbuildvrt canberra-s1s.vrt e*dems*
#gdalwarp canberra-s1s.vrt canberra-s1s.tif
# http://gis.stackexchange.com/questions/1755/how-to-resample-a-batch-of-rasters-using-ogr-gdal
gdalwarp canberra-s1s.vrt canberra-s1s.tif
# original size 10800
#gdalwarp -ts 1600 0 -r cubic -co "TFW=YES" canberra-s1s.vrt canberra-s1s.tif
gdalinfo -mm canberra-s1s.tif
#gdal_translate -scale -86 1898 0 255 -outsize 200 200 -of PNG canberra-s1s.tif canberra-s1s.png
#gdal_translate -scale -86 1898 0 65535 -ot UInt16 -outsize 200 200 -of ENVI canberra-s1s.tif canberra-s1s.bin
gdal_translate -scale -86 1898 0 255 -outsize 2700 2700 -of PNG canberra-s1s.tif canberra-s1s.png
gdal_translate -scale -86 1898 0 65535 -ot UInt16 -outsize 400 400 -of ENVI canberra-s1s.tif canberra-s1s.bin
#gdal_translate -scale -86 1898 0 2000 -ot UInt16 -outsize 675 675 -of ENVI canberra-s1s.tif canberra-s1s.bin

