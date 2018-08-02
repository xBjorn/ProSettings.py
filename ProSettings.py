import requests
from bs4 import BeautifulSoup
import sys


#This is a program that grabs the average setting of CS:GO pro players


#Get the content of the website to calculate the average
r = requests.get("http://csgopedia.com/csgo-pro-setups/")
content = r.content

#We use BeautifulSoup to make it readable for the computers search task
parse = BeautifulSoup
data = parse(r.content, "html.parser")

#Save all the requested data to the arrays to get an average of all dpi's by comparing the arrays
dpi400 = []
dpi450 = []
dpi800 = []
dpi1600 = []

reso1 = []
reso2 = []
reso3 = []

low = data.body.find_all(string="400")
low2 = data.body.find_all(string="450")
medium = data.body.find_all(string="800")
high = data.body.find_all(string="1600")        

findReso1 = data.body.find_all(string="1024 x 768")
findReso2 = data.body.find_all(string="1280 x 960")
findReso3 = data.body.find_all(string="1920 x 1080")

for resolution in findReso1:
    reso1.append(resolution)
for resolution in findReso2:
    reso2.append(resolution)
for resolution in findReso3:
    reso3.append(resolution)

for dpi in low:
    dpi400.append(dpi)
for dpi in low2:
    dpi450.append(dpi)
for dpi in medium:
    dpi800.append(dpi)
for dpi in high:
    dpi1600.append(dpi)

total = len(dpi400) + len(dpi450) + len(dpi800) + len(dpi1600)
totalResos = len(reso1) + len(reso2) + len(reso3)

clow = float(len(dpi400)) / total * 100
clow2 = float(len(dpi450)) / total * 100
cmedium = float(len(dpi800)) / total * 100
chigh = float(len(dpi1600)) / total * 100

creso1 = float(len(reso1)) / totalResos * 100
creso2 = float(len(reso2)) / totalResos * 100
creso3 = float(len(reso3)) / totalResos * 100

print ""
print "{}% uses 400 dpi".format(int(clow))
print "{}% uses 450 dpi".format(int(clow2))
print "{}% uses 800 dpi".format(int(cmedium))
print "{}% uses 1600 dpi".format(int(chigh))
print ""
print "{}% uses 1024 x 768".format(int(creso1))
print "{}% uses 1280 x 960".format(int(creso2))
print "{}% uses 1920 x 1080".format(int(creso3))
