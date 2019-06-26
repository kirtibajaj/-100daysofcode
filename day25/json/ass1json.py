import urllib.request, urllib.parse, urllib.error
import json
import ssl
sum=0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url ='http://py4e-data.dr-chuck.net/comments_249219.json'
html = urllib.request.urlopen(url, context=ctx).read()
data = html
d =json.loads(data)
for item in d['comments']:
    print(item)
    sum+= int(item['count'])
print(sum)
