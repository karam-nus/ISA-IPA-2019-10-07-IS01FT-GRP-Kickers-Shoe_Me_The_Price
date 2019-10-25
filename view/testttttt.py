body = '''<html>
<head>
<title> ABC </title>
<head>
<body>
<table>
<th>Shoe name</th><th>Website name</th><th>Price</th><th>Link</th>
'''
shoe = 'Air max 1'
rows = ''
website = 'Nike'
for i in range(0,12):
     
     row = '''<tr><td>'''+shoe+'''</td><td>'''+website+'''</td></tr>
     '''
     rows += row
     
end = '''</table>
</body>
</html>'''

final = body + rows + end



print(final)
