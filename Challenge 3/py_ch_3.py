# py_ch_3.py
# Python Challenge Page url="http://www.pythonchallenge.com/pc/def/ocr.html"
import re
import urllib

#open url of challenge
f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
#read page source
pageSource = f.read();
#create regular expression for letters
regex = re.compile('[a-zA-Z]+')
#print regex results
print(regex.findall(pageSource))

#Next Challenge Url: http://www.pythonchallenge.com/pc/def/equality.html 
