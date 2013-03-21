# py_ch_2.py
# Python Challenge Page url="http://www.pythonchallenge.com/pc/def/map.html"
from string import maketrans

#input string from python challenge page
input_str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#normal alphabet ordering
intab = "abcdefghijklmnopqrstuvwxyz"
#adjusted alphbet order for cipher
outtab = "cdefghijklmnopqrstuvwxyzab"
#create translation
trantab = maketrans(intab, outtab)
#print result
print input_str.translate(trantab)
#apply on url
print "map.html".translate(trantab)

#Next Challenge Address: http://www.pythonchallenge.com/pc/def/ocr.html