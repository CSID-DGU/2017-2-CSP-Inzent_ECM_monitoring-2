<%@page contentType="text/html; charset=euc-kr" isErrorPage="true"%>
<%response.setStatus(200);%>

<html>
<head>
<title>���� ����</title>
</head>
<body>
<h3>���� �̤�</h3>
���� �޽���: <%=exception.getMessage() %>
</body>
</html>