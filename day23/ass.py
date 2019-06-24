import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
sum=0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_249218.xml'
html = urllib.request.urlopen(url, context=ctx).read()
data = html
tree = ET.fromstring(data)
lst = tree.findall('.//count')
print('User count:', len(lst))
for item in lst:
    sum+= int(item.text)
print(sum)
