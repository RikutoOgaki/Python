import os

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 

str1 = '''
<html>
<head>
<meta charset="utf-8">
<title>{title1}</title>
</head>
<body>
{body1} 
</body>
</html>
'''.format( title1 = "hello html", body1 = "hello html!" ) 

print( str1 ) 

path1 = os.path.dirname(__file__) + "/" 
file1 = path1 + "html1.html" 
write1( file1, str1 ) 