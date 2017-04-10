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
N = 4
menStd =   [0, 0, 0, 0]
#doublecns,doublevow,hashtag,url,
last_wordbefore= [2, 6, 120, 0]
last_word= [2, 6, 383, 237]
last_wordafter = [2, 6, 383, 237]


last_wordbefore_5000= [1050, 1100, 600, 0]
last_word_5000= [900, 1000, 1600, 237]
last_wordafter_5000 = [800, 1000, 1745, 237]
#punc,emot,hashtag,url,mention,rt
#length, lengthword(not added)
tweet=[364, 126, 383, 237, 823, 589]
tweet_5000=[1740, 582, 1745, 1825, 1757, 2934]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars


#############
#Word Before-2
rects4 = ax.bar(ind, last_wordbefore, width,
                color='black',
                yerr=menStd,
                error_kw=dict(elinewidth=5,ecolor='red'))
#Word-2
rects5 = ax.bar(ind+width, last_word, width,
                color='red',
                yerr=menStd,
                error_kw=dict(elinewidth=5,ecolor='black'))
#Word After-2
rects6 = ax.bar(ind+width*2, last_wordafter, width,
                color='blue',
                yerr=menStd,
                error_kw=dict(elinewidth=5,ecolor='black'))
#Tweet
#rects7 = ax.bar(ind+width*4, tweet, width,
#                color='blue',
#                yerr=menStd,
#                error_kw=dict(elinewidth=5,ecolor='black'))



# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,1500)
ax.set_ylabel('Features')
ax.set_title('Features by Word Before,Word and Word After')
xTickMarks = ['Feature'+str(i) for i in range(1,5)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)


#2nd
ax.legend( (rects4[0], rects5[0], rects6[0]), ('Word Before', 'Word', 'Word After','Tweet') )
#Tweet
#ax.legend((rects7[0]), ('Tweet'))

plt.show()