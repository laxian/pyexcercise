#!/usr/bin/python

import re
pa=re.compile(r'(\w{6,})@(\w+.com)')
ma=pa.match('laxian2010@qq.com')
print(ma.group())
print(ma.group(0))
print(ma.groups()[1])