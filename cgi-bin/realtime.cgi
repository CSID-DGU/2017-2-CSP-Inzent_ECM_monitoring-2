#!/usr/bin/python
# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import sqlalchemy as sql
from mpld3 import fig_to_html
import matplotlib.pyplot as plt
import cgi, cgitb
cgitb.enable()
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
conn = sql.create_engine(local)

form = cgi.FieldStorage()
m = int(form.getvalue('m'))
s = int(form.getvalue('s'))

df = pd.read_sql('select * from future where minute * 60 + second >= ' + str((m-2)*60+s) + ' and minute*60+second < ' + str(m*60+s), conn)
df = df.groupby(['VOLUMEID', 'minute', 'second'])['FILESIZE'].sum()

sz = 60
vol1 = []
vol2 = []
total = []
for i in range(sz):
    vol1.append(df[i]/1000000)
    vol2.append(df[i+sz]/1000000)
    total.append((df[i]+df[i+sz])/1000000)
for i in range(len(vol1), sz): vol1.append(0)
for i in range(len(vol2), sz): vol2.append(0)
for i in range(len(total), sz): total.append(0)

plt.style.use('fivethirtyeight')
xlabel = [x - sz for x in range(sz)]
print 'Content-type: text/html;\r\n\r\n'
for i in range(sz):
    plt.plot(xlabel, total[i:i+sz])
    plt.plot(xlabel, vol1[i:i+sz])
    plt.plot(xlabel, vol2[i:i+sz])
    plt.legend(['Total', 'storage1', 'storage2'])
    plt.ylabel('Gbyte')
    plt.xlabel('time(sec)')
    fig = plt.gcf()
    fig.set_size_inches(12,4)
    plt.savefig('../file/' + str(i) + '.png')
    plt.clf()
