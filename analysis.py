# -*- coding: utf-8 -*-
# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

rows =[]
f = open('filteredlist.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
finally:
    f.close()

df = pd.read_csv('filteredlist.csv' , names=['id', 'word', 'tagType', 'sentencenumber'])

personCount , locationCount , organizationCount, productCount= 0,0,0,0
dateCount , moneyCount , percentCount ,otherCount= 0,0,0,0



for i in range(0, len(df) - 1):
    if df.tagType[i] == 'Person':
        personCount += 1
    elif df.tagType[i] == 'Location':
        locationCount += 1
    elif df.tagType[i] == 'Organization':
        organizationCount += 1
    elif df.tagType[i] == 'Product':
        productCount += 1
    elif df.tagType[i] == 'Date':
        dateCount += 1
    elif df.tagType[i] == 'Money':
        moneyCount += 1
    elif df.tagType[i] == 'Percent':
        percentCount += 1
    else:
        otherCount += 1

tagTypes = ['Person' , 'Location' , 'Organization' , 'Product' , 'Date' , 'Money' , 'Percent']


counter = [personCount, locationCount,organizationCount, productCount,dateCount, moneyCount,percentCount]
list = {'tagTypes':tagTypes,'counter': counter}
df_taglist =pd.DataFrame(list)

print df_taglist

print "***Max value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== max(df_taglist.counter)].index]

print "\n***Min value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== min(df_taglist.counter)].index]

print "\n***Mean of tagged word:",df_taglist.mean()

print "\n***Standart deviation of tagged word:",df_taglist.std()


plt.plot([1,2,3,4,5,6,7], counter, 'ro')
plt.axis([0, 8, 0, 3500])
#plt.show()
plt.title("Tag Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()




