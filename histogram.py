# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 5
#letter, capital, allcapital, punct, emot
first_fivefeature_wb = [28, 19, 34, 143, 80]
menStd =   [0, 0, 0, 0, 0]
first_fivefeature_w = [27, 19, 34, 143, 126]
first_fivefeature_wa = [27, 19, 33, 144, 126]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars

## the bars
#Word Before
rects1 = ax.bar(ind, first_fivefeature_wb, width,
                color='black',
                yerr=menStd,
                error_kw=dict(elinewidth=10,ecolor='red'))
#Word
rects2 = ax.bar(ind+width, first_fivefeature_w, width,
                    color='red',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10,ecolor='black'))
#Word After
rects3 = ax.bar(ind+width*2, first_fivefeature_wa, width,
                    color='blue',
                    yerr=menStd,
                    error_kw=dict(elinewidth=10,ecolor='black'))

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,150)
ax.set_ylabel('Features')
ax.set_title('Features by Word Before,Word and Word After')
xTickMarks = ['Feature'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Word Before', 'Word', 'Word After') )
plt.show()
