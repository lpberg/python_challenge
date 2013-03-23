# py_ch_4.py
# Python Challenge Page url="http://www.pythonchallenge.com/pc/def/equality.html"
import re
import urllib

#open page source
f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html ")
#read page source
pageSource = f.read();
#create regular expression for one small letter surrounded by 3 large ones
regex = re.compile('[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]')
#run regular expression on page source
results = regex.findall(pageSource)
#print results
for i in results: 
	print i[4]
    
#Next Challenge Url: http://www.pythonchallenge.com/pc/def/linkedlist.html

