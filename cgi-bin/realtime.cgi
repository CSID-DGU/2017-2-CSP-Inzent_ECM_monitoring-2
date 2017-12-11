#!/usr/bin/python
# coding: utf-8
import pandas as pd
import sqlalchemy as sql
import matplotlib.pyplot as plt
import cgitb, datetime, os
cgitb.enable()
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
conn = sql.create_engine(local)

now = datetime.datetime.now();
m = now.minute
s = now.second
f = ''
if os.stat('file/0.png').st_mtime < os.stat('file/1.png').st_mtime: f = '0'
else: f = '1'

df = pd.read_sql('select * from future where minute * 60 + second >= ' + str((m-2)*60+s) + ' and minute*60+second < ' + str(m*60+s), conn)
df = df.groupby(['VOLUMEID', 'minute', 'second'])['FILESIZE'].sum()

sz = len(df)/2
vol1 = []
vol2 = []
total = []
label = [x for x in range(sz)]
for i in range(sz):
    vol1.append(df[i]/1000)
    vol2.append(df[i+sz]/1000)
    total.append((df[i]+df[i+sz])/1000)

plt.style.use('fivethirtyeight')
plt.plot(vol1)
plt.plot(vol2)
plt.plot(total)
plt.axis('off')
fig = plt.gcf()
fig.set_size_inches(18,4)
plt.savefig('file/' + f + '.png', transparent=True)
