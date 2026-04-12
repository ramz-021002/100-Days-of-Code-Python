from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.content, 'lxml')

movies = soup.find_all('strong')

# for movie in movies:
#     print(movie.get('strong'))


movie_titles = []
for movie in movies:
    if movie not 'Director:' and movie not 'Starring:':
        movie_titles.append(movie.text)

print(movie_titles)

