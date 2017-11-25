<%@page contentType="text/html; charset=euc-kr" isErrorPage="true"%>
<%response.setStatus(200);%>

<html>
<head>
<title>데베 에러</title>
</head>
<body>
<h3>에러 ㅜㅜ</h3>
에러 메시지: <%=exception.getMessage() %>
</body>
</html>