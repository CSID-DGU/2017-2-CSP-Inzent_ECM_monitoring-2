<%@page contentType="text/html; charset=euc-kr" errorPage="DBError.jsp"%>
<%@page import="java.sql.*"%>

<%!
Connection conn=null;
Statement stmt1=null;
Statement stmt2=null;
ResultSet rs1=null;
ResultSet rs2=null;
%>

<html>
<head><title>남은 용량 그래프</title></head>
<body>
<%
try{
Class.forName("com.mysql.jdbc.Driver");
conn=DriverManager.getConnection("jdbc:mysql://inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com:3306/inzent", "inzent", "1q2w3e4r!");

if (conn==null)
 throw new Exception("데이터베이스에 연결할 수 없습니다.<br>");

stmt1=conn.createStatement();
rs1=stmt1.executeQuery("SELECT MAXSPACE-SPACELEFT, SPACELEFT FROM ASYSVOLUME WHERE VOLUMEID='1HS_V001';");
if(rs1.next()){
float using1=rs1.getFloat("MAXSPACE-SPACELEFT");
float left1=rs1.getFloat("SPACELEFT");

request.setAttribute("USING1", using1);
request.setAttribute("LEFT1", left1);
}

stmt2=conn.createStatement();
rs2=stmt2.executeQuery("SELECT MAXSPACE-SPACELEFT, SPACELEFT FROM ASYSVOLUME WHERE VOLUMEID='2HS_V001';");
if(rs2.next()){
float using2=rs2.getFloat("MAXSPACE-SPACELEFT");
float left2=rs2.getFloat("SPACELEFT");

request.setAttribute("USING2", using2);
request.setAttribute("LEFT2", left2);
}
}
finally{
try{
stmt1.close();
stmt2.close();
conn.close();
}
catch(Exception ignored){
}
}
RequestDispatcher dispatcher=request.getRequestDispatcher("pie_test.jsp");
dispatcher.forward(request, response);
%>
</body>
</html>
