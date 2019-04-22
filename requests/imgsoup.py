import re

from bs4 import BeautifulSoup
import requests as rq
import os

url='https://www.4493.com/motemeinv/'
res=rq.get(url)
soup=BeautifulSoup(res.content,"html.parser")


def filename(url):
    return url[url.rfind('/') + 1:]


def folder(url):
    restr = 'https?://(?P<host>[\w\.]+)/.+?.jpg'
    p = re.compile(restr)
    m = p.match(url)
    if m is None:
        return 'imgs'
    return m.group('host')


def savefile(url):
    print(url)
    fold = folder(url)
    if not os.path.exists(fold):
        os.mkdir(fold)
    f = open(fold + os.sep + filename(url), 'wb+')
    f.write(rq.get(url=url).content)
    f.close()


for i in soup.find_all('img'):
    img_url=''
    if i.has_key('lazysrc'):
        img_url=i['lazysrc']
    elif i.has_key('src'):
        img_url=i['src']

    if img_url.startswith('http'):
        savefile(img_url)
