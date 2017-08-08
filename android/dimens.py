#! /usr/bin/python
import re

path = '/Users/leochou/StudioProjects/DywTeacher/app/src/main/res/values/dimens.xml'

mulriple = 1.5

density=(1.0,1.5,2,3,4)

def dimens(ratio):

	def convert(match):
		return re.sub('\d+', convert2, match.group())

	def convert2(match):
		return str(int(match.group())*ratio)

	f = open(path, 'r')
	out=open(str(mulriple/ratio)+'.xml','w+')
	lines=f.readlines()
	for l in lines:
		out.write(re.sub('\d+((d|s)p|px)', convert, l))
	f.close()
	out.close()

for r in density:
	ratio=mulriple/r
	dimens(ratio)
