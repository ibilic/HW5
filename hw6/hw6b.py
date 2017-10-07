import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def numlink(url, num):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    return tags[num-1]
url = input('Enter URL: ')
# url =  "http://py4e-data.dr-chuck.net/known_by_Rayane.html"
count = int(input('Enter Count: '))
Position = input('Enter Position: ')
for link in range(count):
    tag = numlink(url, int(Position)) #tag = numlink(url, int(input('Enter Position: ')))
    url = tag.get('href') #I didn't implement input because it would be awful to grade
    print ('Retrieving: ', url)
print ('Last name retreived: ', tag.contents[0])
