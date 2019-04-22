
from bs4 import BeautifulSoup
import requests
import re
import os


class Spider(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        self.headers = {'User_agent': self.user_agent}

    def gettxt(self, url):
        response = requests.get(url=url, headers=self.headers)
        response.encoding='utf-8'
        return response.text

    def filter(self, restr, txt):
        p = re.compile(restr)
        return p.findall(txt)

    def savefile(self, url):
        print(url)
        folder=self.folder(url)
        if not os.path.exists(folder):
            os.mkdir(folder)
        f = open(folder+os.sep+self.filename(url), 'wb+')
        f.write(requests.get(url=url, headers=self.headers).content)
        f.close()

    def imgs(self, url):
        content = self.gettxt(url)
        soup=BeautifulSoup(content,'html.parser')
        all_imgs=soup.find_all('img')
        for i in all_imgs:
            if i.has_attr('onload'):
                self.savefile(i['src'])

        nexttag = soup.find(id='nextpage')
        nextref = nexttag.get('href')
        regex = 'javascript:gotourl\(\'(.+)\'\)'
        p = re.compile(regex)
        m = p.match(nextref)
        nexturl = m.group(1)

        if self.filename(url) != nexturl:
            self.imgs(url[:url.rfind('/')+1]+nexturl)
        else:
            all_a=soup.find_all('a')
            for a in all_a:
                if a.has_attr('href') and re.match('[/\w+]+/\d.(htm|html)',a['href']):
                    self.imgs(self.host(url)+a['href'])


    def filename(self, url):
        return url[url.rfind('/')+1:]

    def folder(self, url):
        restr='https?://(?P<host>[\w\.]+)/.+?.jpg'
        p=re.compile(restr)
        m=p.match(url)
        if m is None:
            return 'imgs'
        return m.group('host')

    def host(self, url):
        return url[:url.find('/', url.find('://')+3)]


spider=Spider()
# spider.imgs('https://www.4493.com/weimeixiezhen/126686/1.htm')
spider.imgs('https://www.4493.com/tiyumeinv/117610/1.htm')
# spider.savefile('http://i2.douguo.net/upload/shicai/1446100499.jpg')


