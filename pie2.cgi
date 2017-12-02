#!C:\Python27\python.exe
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import cgi, cgitb
import mpld3 as d3
import sqlalchemy as sql
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

cgitb.enable()

form=cgi.FieldStorage()
formm=form.getvalue('kind')

conn=sql.create_engine('mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com:3306/inzent')

query=pd.read_sql("select MAXSPACE-SPACELEFT, SPACELEFT from ASYSVOLUME", conn)
using1=round(query.iloc[0][0]/1073741824,3)
left1=round(query.iloc[0][1]/1073741824,3)
using2=round(query.iloc[1][0]/1073741824,3)
left2=round(query.iloc[1][1]/1073741824,3)

ul0=[using1+using2, left1+left2]
label=['using','left']

a=plt.figure()
DPI = a.get_dpi()
a.set_size_inches(2300.0/float(DPI),800.0/float(DPI))

#plt.style.use('dark_background') 디자인고민...
mpl.rcParams['font.size']=20

if formm=="pie" :

    ul1=[using1, left1]
    ul2=[using2, left2]
    
    plt.subplot(132, fc="none")
    plt.pie(ul1, labels=[str(using1)+'GB', str(left1)+'GB'], autopct='%1.1f%%')
    plt.title('1st archive')

    plt.subplot(133, fc="none")
    plt.pie(ul2, labels=[str(using2)+'GB', str(left2)+'GB'], autopct='%1.1f%%')
    plt.title('2nd archive')

    plt.subplot(131, fc="none")
    plt.pie(ul0, labels=[str(ul0[0])+'GB', str(ul0[1])+'GB'], autopct='%1.1f%%')
    plt.title('total archives')
    plt.legend(label, loc="upper left")


elif formm=="bar":
    archive=['total archives', '1st archive', '2nd archive']
    ind=[x for x, _ in enumerate(archive)]
    using=np.array([using1+using2, using1, using2])
    left=np.array([left1+left2, left1, left2])
    total=using+left
    pro_using=np.true_divide(using, total)*100
    pro_left=np.true_divide(left, total)*100
 
    plt.bar(ind, pro_using, width=0.4, bottom=pro_left)
    plt.bar(ind, pro_left, width=0.4)

    plt.xticks(ind, archive)
    plt.ylim=1.0
    plt.legend(label, loc="lower left")

    for i,j in zip(ind, left):
        plt.annotate(str(j)+'GB',xy=(i-0.05,pro_left[i]-5))
        plt.annotate(format(pro_left[i],'1.1f')+'%',xy=(i-0.025,pro_left[i]-10))
    for i,j in zip(ind, using):
        plt.annotate(str(j)+'GB',xy=(i-0.05,95))
        plt.annotate(format(pro_using[i],'1.1f')+'%',xy=(i-0.025,90))


print 'Content-type: text/html;\n'
print d3.fig_to_html(a)
