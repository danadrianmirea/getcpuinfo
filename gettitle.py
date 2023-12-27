
from urllib.request import urlopen

url = 'https://www.cpubenchmark.net/cpu.php?cpu=i7-5600'
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_s = html.find("<div class>")
title_e = html.find("</title>")

title = html[title_s:title_e]

print(title)


