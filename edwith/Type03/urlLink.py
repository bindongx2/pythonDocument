import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#https 작동가능(소스)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#https 작동가능(소스)

url = input('Enter - ')
#http://www.dr-chuck.com/page1.htm
#https://www.si.umich.edu/
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#a 태그 href속성값 찾기
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
