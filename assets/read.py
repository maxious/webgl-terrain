import sys
from struct import *
from stl_tools import numpy2stl
from stl_tools.cwrapped import tessellate #optional but faster
from numpy  import *
import os

width = int(sys.argv[1])
print "width: %d" % width
#height = int(sys.argv[2])
height = 65535
print "max height: %d" % height

filesize = os.path.getsize("canberra-s1s.bin")

with open("canberra-s1s.bin", "rb") as f:
    a = []
    y = []
    bytes_read = 0
    word = f.read(2)
    while word != "":
	raw = float(unpack('h',word)[0])
	value = abs(raw /height * 100)
	
	#print '%d,%d,%f' % (x,y,value)
	y.append(value)

	if len(y) >= width:
	    a.append(y)
	    y = []
        word = f.read(2)
	bytes_read = bytes_read + 2
	if floor(bytes_read / 10000) % 10 == 0:
		sys.stdout.write("\r %d / %d (%f)" % (bytes_read, filesize, ((bytes_read/filesize)*100 )))
		sys.stdout.flush()

A=array(a)

numpy2stl(A, "out.stl", scale=0.5, solid=False)
