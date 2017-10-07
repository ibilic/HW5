import urllib.request, urllib.parse, urllib.error
# import urlopen
from bs4 import BeautifulSoup
import re

# url = 'http://py4e-data.dr-chuck.net/comments_31492.html'
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags

tags = soup('span')
sum_total = 0
count = 0
for tag in tags:
   # Look at the parts of a tag
	# print ('Contents:',tag.contents[0])
	num = int(tag.contents[0])
	sum_total += num
	count += 1
print ('Count: ', count)
print ('Sum: ', sum_total)
