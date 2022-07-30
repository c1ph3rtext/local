import requests as req
import re
import sys

uagent = {"User-Agent":"Mozilla/4.0 (Windows NT 7.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

url = sys.argv[1]
r = req.get(url, headers=uagent)
s = r.text
urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
for i in urls:
    if i.startswith("http"):
       print(i)
    else: continue
