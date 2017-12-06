#!/usr/bin/python
#-*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import mpld3 as d3
import sqlalchemy as sql

local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
conn=sql.create_engine(local)
df = pd.read_sql("select MAXSPACE-SPACELEFT, SPACELEFT from ASYSVOLUME", conn)

vol1 = [df.iloc[0][0], df.iloc[0][1]]
vol2 = [df.iloc[1][0], df.iloc[1][1]]
labels = ['Used', 'Free']
colors = ['red', 'deepskyblue']
explode = [0.1, 0]

#plt.style.use('bmh')
plt.subplot('131')
plt.title('Storage1', fontsize=15)
plt.pie(vol1, explode = explode,labels = labels, autopct = '%1.1f%%', startangle=-90, colors=colors)
plt.subplot('132')
plt.title('Storage2', fontsize=15)
plt.pie(vol2, explode = explode,labels = labels, autopct = '%1.1f%%', startangle=-90, colors=colors)
plt.subplot('133')
plt.title('Total', fontsize=15)
plt.pie([sum(x) for x in zip(vol1, vol2)], explode = explode,labels = labels, autopct = '%1.1f%%', startangle=-90, colors=colors)
fig = plt.gcf()
fig.set_size_inches(12, 4)
#plt.show()
print 'Content-type:text/html;\r\n\r\n'
print d3.fig_to_html(fig)
