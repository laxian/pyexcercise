#!/usr/bin/python

from math import sqrt as sq
from sys import argv

def dpi(w,h,d):
	return sq(w**2+h**2)/(d*1.0)
for a in argv:
	print (a)

self,w,h,d=argv
print (dpi(int(w),int(h),int(d)))

