#!"C:\Users\whn12\AppData\Local\Programs\Python\Python38-32\python.exe"
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi
form = cgi.FieldStorage()
title = form.getvalue("title")
description = form.getvalue("description")

opend_file = open('data/'+title, 'w', encoding='utf-8')
opend_file.write(description)
opend_file.close()

print("Location: index.py?id="+title)
print()
