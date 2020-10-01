#!"C:\Users\whn12\AppData\Local\Programs\Python\Python38-32\python.exe"
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r', encoding='utf-8').read()
else:
    pageId = 'City Pop'
    description = "City pop (シティーポップ, shitī poppu) is a loosely defined subset of pop music that <u>originated in Japan in the late 1970s.</u> It was originally termed as an offshoot of Japan\'s Western-influenced <strong> \'new music\',</strong> but came to include a wide range of styles associated with the country\'s nascent economic boom, such as AOR, soft rock, R&B, funk, and boogie. It was also associated with new emerging technologies, such as the Walkman, cars with built-in cassette decks and FM stereos, and various electronic musical instruments. There is no unified consensus among scholars regarding the definition of city pop. In Japan, the tag simply referred to a broad array of artists that were considered to project an \"urban\" feel. In other words, \"music made by city people, for city people.\" Most of these artists refused to embrace Japanese influences, and instead, largely drew from American soft rock, boogie, and funk. Some examples may also feature tropical flourishes or elements taken from disco, jazz fusion, Latin, Caribbean, or Polynesian music."
print('''<!doctype html>
<html>
  <head>
    <title>WEB1 - Welcome</title>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="style.css">
    <script src="colors.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  </head>
  <body>
    <h1><a href="index.py">City Pop</a></h1>
    <div id ="grid">
      <ol>
        {listStr}
      </ol>
      <div id="article">
      <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
      </form>
      </div>
  </div>
  <input type="button" value="night" onclick="
    nightDayHandler(this);
  ">
  </body>
</html>
'''.format(
    title=pageId,
    desc=description,
    listStr=view.getList()))
