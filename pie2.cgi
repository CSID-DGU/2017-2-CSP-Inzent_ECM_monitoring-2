#!C:\Python27\python.exe
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import cgi
import cgitb
import mpld3 as d3
import sqlalchemy as sql
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

cgitb.enable()

form=cgi.FieldStorage()
formm=form.getvalue('kind')

conn=sql.create_engine('mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com:3306/inzent')

query1=pd.read_sql("select MAXSPACE-SPACELEFT, SPACELEFT from ASYSVOLUME where VOLUMEID='1HS_V001'", conn)
using1=query1.iloc[0][0]
left1=query1.iloc[0][1]
ul1=[using1, left1]

query2=pd.read_sql("select MAXSPACE-SPACELEFT, SPACELEFT from ASYSVOLUME where VOLUMEID='2HS_V001'", conn)
using2=query2.iloc[0][0]
left2=query2.iloc[0][1]
ul2=[using2, left2]

ul0=[using1+using2, left1+left2]

label=['using','left']

if formm=="pie" :

    a=plt.figure()
    
    DPI = a.get_dpi()
    a.set_size_inches(2300.0/float(DPI),800.0/float(DPI))    

    plt.subplot(132)
    plt.pie(ul1, labels=[str(using1)+'byte', str(left1)+'byte'], autopct='%1.1f%%')
    plt.title('1st archive')

    plt.subplot(133)
    plt.pie(ul2, labels=[str(using2)+'byte', str(left2)+'byte'], autopct='%1.1f%%')
    plt.title('2nd archive')

    plt.subplot(131)
    plt.pie(ul0, labels=[str(ul0[0])+'byte', str(ul0[1])+'byte'], autopct='%1.1f%%')
    plt.title('total')
    plt.legend(label, loc="upper left")


elif formm=="bar":
    r = [0,1,2]
    rr=[0.4, 1.4, 2.4]
    using=[ul0[0], using1, using2]
    left=[ul0[1], left1, left2]
 
    names = ['total','1st archive','2nd archive']
    
    a=plt.figure()

    DPI = a.get_dpi()
    a.set_size_inches(2300.0/float(DPI),800.0/float(DPI))
    
    plt.barh(r, using, height=0.3)
    plt.barh(rr, left, height=0.3)

    plt.yticks([0.2,1.2,2.2], names)
    plt.xlim(0, sum(ul0))
    plt.xlabel("(unit: byte)")
    plt.legend(label, loc="lower right")
    plt.gca().invert_yaxis()

    for i,j in zip(using, r):
        plt.annotate(str(i),xy=(i,j))
    for i,j in zip(left, rr):
        plt.annotate(str(i),xy=(i,j))

print 'Content-type: text/html;\n'
print d3.fig_to_html(a)
