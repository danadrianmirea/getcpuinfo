# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.cpubenchmark.net/cpu.php?cpu=i7-5600'
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div")

for div in divs:
    print(div)
