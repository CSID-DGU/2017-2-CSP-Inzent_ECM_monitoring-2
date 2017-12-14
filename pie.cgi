#!C:\Python27\python.exe
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import cgi
import cgitb
import mpld3 as d3
import sqlalchemy as sql
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

cgitb.enable()

#form=cgi.FieldStorage()
#formm=form.getvalue('kind')
formm="pie"

conn=sql.create_engine('mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com:3306/inzent?charset=utf8')

query=pd.read_sql("select MAXSPACE-SPACELEFT, SPACELEFT from ASYSVOLUME", conn)
using1=round(query.iloc[0][0]/1073741824,3)
remain1=round(query.iloc[0][1]/1073741824,3)
using2=round(query.iloc[1][0]/1073741824,3)
remain2=round(query.iloc[1][1]/1073741824,3)

ul0=[using1+using2, remain1+remain2]
label=['using','remain']

a=plt.figure()
DPI = a.get_dpi()
a.set_size_inches(2300.0/float(DPI),800.0/float(DPI))

plt.style.use('fivethirtyeight')
mpl.rcParams['font.size']=20

if formm=="pie" :

    ul1=[using1, remain1]
    ul2=[using2, remain2]
    
    plt.subplot(132, facecolor="none")
    plt.pie(ul1, labels=[str(using1)+'GB', str(remain1)+'GB'], autopct='%1.1f%%')
    plt.title('storage1')
    
    plt.subplot(133, facecolor="none")
    plt.pie(ul2, labels=[str(using2)+'GB', str(remain2)+'GB'], autopct='%1.1f%%')
    plt.title('storage2')

    plt.subplot(131, facecolor="none")
    plt.pie(ul0, labels=[str(ul0[0])+'GB', str(ul0[1])+'GB'], autopct='%1.1f%%')
    plt.title('Total')
    plt.legend(label, loc="upper left")


elif formm=="bar":
    archive=['Total', 'storage1', 'storage2']
    ind=[x for x, _ in enumerate(archive)]
    using=np.array([using1+using2, using1, using2])
    remain=np.array([remain1+remain2, remain1, remain2])
    total=using+remain
    pro_using=np.true_divide(using, total)*100
    pro_remain=np.true_divide(remain, total)*100
    
    plt.subplot(facecolor="none")
    plt.bar(ind, pro_using, width=0.4, bottom=pro_remain)
    plt.bar(ind, pro_remain, width=0.4)

    plt.xticks(ind, archive)
    plt.ylim=1.0
    plt.legend(label, loc="lower left")

    for i,j in zip(ind, remain):
        plt.annotate(str(j)+'GB',xy=(i-0.05,pro_remain[i]-5))
        plt.annotate(format(pro_remain[i],'1.1f')+'%',xy=(i-0.025,pro_remain[i]-10))
    for i,j in zip(ind, using):
        plt.annotate(str(j)+'GB',xy=(i-0.05,95))
        plt.annotate(format(pro_using[i],'1.1f')+'%',xy=(i-0.025,90))


print 'Content-type: text/html;\n'
print d3.fig_to_html(a)
