import re
import requests
import hashlib


url="http://docker.hackthebox.eu:30649/"
qingqiu=requests.session()
outhtml=qingqiu.get(url)
print (outhtml.text)
pipei = re.compile(r"<h3 align='center'>(*)</h3>")
str = pipei.findall(outhtml.text)
print (type(str))
print (str)
postmd5=hashlib.md5(str[0]).hexdigest()
print (postmd5)
data={'hash': postmd5}
postout = qingqiu.post(url=url, data=data)




print(postout.text)


