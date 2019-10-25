def mail_template(df):

	body = '''<html>
	<head>
	<title> ABC </title>
	</head>
	<body>
	<table border = "6" style = "background : linear-gradient(to right, #0099ff -81%, #ffffff 100%)" width = 600 height = 600>
	<th>Shoe name</th><th>Website name</th><th>Price</th><th>Colorware</th>
	'''

	rows = ''

	for i in range(0,len(df)):
	     
	     row = '''<tr ><td align = "center" style="font-family:cursive;">'''+df["name"][i]+'''</td><td align = "center" style="font-family:cursive;">'''+df["Company"][i]+'''</td><td align = "center" style="font-family:cursive;">'''+df["price"][i]+'''</td>
	     <td align = "center"><img src =''' + df["img"][i] + '''width = 100 height = 100/></td></tr>
	     '''
	     rows += row
	     
	end = '''</table>
	</body>
	</html>'''

	final = body + rows + end

	return final
