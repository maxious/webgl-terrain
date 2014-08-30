import sys
from struct import *

with open("canberra-s1s.bin", "rb") as f:
    x = 0
    y = 0
    word = f.read(2)
    while word != "":
	raw = float(unpack('h',word)[0])
	value = abs(raw /65535*100)
	print '%d,%d,%f' % (x,y,value)
	x = x + 1
	if x >= 200:
	    y = y + 1
	    x = 0
        word = f.read(2)
