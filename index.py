#!"C:\Users\whn12\AppData\Local\Programs\Python\Python38-32\python.exe"
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer
sanitize = html_sanitizer.Sanitizer()


form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r', encoding='utf-8').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'City Pop'
    description = "City pop (シティーポップ, shitī poppu) is a loosely defined subset of pop music that <u>originated in Japan in the late 1970s.</u> It was originally termed as an offshoot of Japan\'s Western-influenced <strong> \'new music\',</strong> but came to include a wide range of styles associated with the country\'s nascent economic boom, such as AOR, soft rock, R&B, funk, and boogie. It was also associated with new emerging technologies, such as the Walkman, cars with built-in cassette decks and FM stereos, and various electronic musical instruments. There is no unified consensus among scholars regarding the definition of city pop. In Japan, the tag simply referred to a broad array of artists that were considered to project an \"urban\" feel. In other words, \"music made by city people, for city people.\" Most of these artists refused to embrace Japanese influences, and instead, largely drew from American soft rock, boogie, and funk. Some examples may also feature tropical flourishes or elements taken from disco, jazz fusion, Latin, Caribbean, or Polynesian music."
    update_link = ''
    delete_action = ''
print('''<!doctype html>
<html>
  <head>
    <title>WEB1 - {title}</title>
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
        <h2>{title}</h2>
        <p>
        {desc}
        </P>
         <a href="create.py">create</a>
         {update_link}
         {delete_action}
      </div>
  </div>
  <input type="button" value="night" onclick="
    nightDayHandler(this);
  ">
  </body>
</html>
'''.format(
    title=title,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))
