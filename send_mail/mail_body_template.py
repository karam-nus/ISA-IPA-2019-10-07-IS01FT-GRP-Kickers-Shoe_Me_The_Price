def mail_template(df):
    df.reset_index(inplace=True)
    body = '''<html>
	<head>
	<title> ABC </title>
	</head>
	<body>
	<table border = "6" style = "background : linear-gradient(to right, #ccff99 0%, #ffffff 100%)" width = 600 height = 600>
	<th>Shoe name</th><th>Website name</th><th>Price</th><th>Colorware</th><th>Recommendation</th>
	'''

    rows = ''
    # print('[mbt]a')
    for i in range(0, len(df)):

        row = '''<tr ><td align = "center" style="font-family:Helvetica;"><a href = '''+df["link"][i]+'''>'''+df["name"][i]+'''</a></td><td align = "center" style="font-family:Helvetica;">'''+df["Company"][i]+'''</td><td align = "center" style="font-family:Helvetica;">'''+df["price"][i]+'''</td>
	     <td align = "center"><img src =''' + df["img"][i] + ''' width = 100 height = 100/></td><td>''' + df["trend"][i]+'''</tr>
	     '''
        # print('[mbt]a',i,row)
        # print('[mbt]b',df['name'][i],df['img'][i])
        # print('[mbt]b')
        rows += row
        # print('===[mbt]c',i+1," rows completed")

    end = '''</table>
	</body>
	</html>'''

    final = body + rows + end
    # print('[mbt]c')
    return final
