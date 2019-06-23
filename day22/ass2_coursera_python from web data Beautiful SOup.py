import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Aun.html'
count = 7
position = 18-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')
for i in range(count):
    link = href[position].get('href', None)
    x=href[position].contents[0]
    print(x)
    url='http://py4e-data.dr-chuck.net/known_by_'+x+'.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
