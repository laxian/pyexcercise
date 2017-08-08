import urllib.request
import urllib.parse
import requests

URL_IP = 'http://127.0.0.1:8000/get'

def use_simple_urllib2():
    response = urllib.request.urlopen(URL_IP)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read().decode('UTF-8'))

def use_params_urllib2():
    params = urllib.parse.urlencode({'user':'laxian','age':'29'})
    response = urllib.request.urlopen('?'.join([URL_IP, params]))
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read().decode('UTF-8'))

if __name__ == '__main__':
    print('>>>Use simple urllib2:')
    # use_simple_urllib2()
    use_params_urllib2()