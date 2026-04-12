import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in the YYYY-MM-DD format: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64 AppleWebKit/537.36 (KHTML, like Gecko) Chrime/135.0.0.0 Safari/537.3.6"}

request = requests.get("https://www.billboard.com/charts/hot-100/" + date, headers=header)

soup = BeautifulSoup(request.content, "html.parser")
titles = soup.select("ul.lrv-a-unstyle-list li.o-chart-results-list__item h3.c-title")

song_names = []

for t in titles:
    name = t.get_text(strip=True)
    if name:  # avoid empty ones
        song_names.append(name)


print(song_names)