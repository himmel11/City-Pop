#!"C:\Users\whn12\AppData\Local\Programs\Python\Python38-32\python.exe"
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi, os
form = cgi.FieldStorage()
pageId = form.getvalue("pageId")

os.remove('data/'+pageId)

print("Location: index.py")
print()
