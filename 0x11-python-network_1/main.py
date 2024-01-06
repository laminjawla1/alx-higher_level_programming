import shutil
import tempfile
import urllib.parse
import urllib.request


# with urllib.request.urlopen('http://python.org') as response:
#     html = response.read()
#     print(html)

# with urllib.request.urlopen('http://laminjawla.tech') as response:
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         shutil.copyfileobj(response, tmp_file)
# with open(tmp_file.name) as html:
#     text = html.readlines()
#     for line in text:
#         print(line.strip())

# Data
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {
    'name' : "Lamin Jawla",
    'ocation' : 'The Gambia',
    'language' : 'Python'
}

# data = urllib.parse.urlencode(values)
# data = data.encode('ascii')
# req = urllib.request.Request(url, data, headers={"name" : "Sage", "age" : 26, "spouse": "Mariama"})
# with urllib.request.urlopen(req) as response:
#     page = response.read()


import requests


response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Eopsaltria_australis_-_Mogo_Campground.jpg/640px-Eopsaltria_australis_-_Mogo_Campground.jpg')
with open("bird.jpg", "wb") as bin_writer:
    bin_writer.write(response.content)
print(response.content)