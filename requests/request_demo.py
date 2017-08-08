import requests


URL_GET = 'http://127.0.0.1:8000/get'
URL_IP = 'http://127.0.0.1:8000/ip'

def use_simple_requests():
    response = requests.get(URL_IP)
    print('>>>Response Headers:')
    print(response.headers)
    print('>>>Response Body:')
    print(requests.text)

# def use_params_requests():
#     params = urllib.parse.urlencode({'user':'laxian','age':'29'})
#     response = urllib.request.urlopen('?'.join([URL_IP, params]))
#     print('>>>Response Headers:')
#     print(response.info())
#     print('>>>Response Body:')
#     print(response.read().decode('UTF-8'))

if __name__ == '__main__':
    print('>>>Use simple urllib2:')
    use_simple_requests()
    #use_params_urllib2()
