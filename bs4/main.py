from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title.string)

# all_anchor = soup.find_all(name='a')
#
# for anchor in all_anchor:
#     print(anchor.get('href'))
    # print(anchor.text)
#
# heading = soup.find(name='h1', id='name')
# print(heading.text)

import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

soup = BeautifulSoup(response.text, "lxml")

articles = soup.find_all(name='a', class_="storylink")
articles_upvote = soup.find_all(name='span', class_="score")

article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    article_texts.append(article.text)
    article_links.append(article.get('href'))

for article in articles_upvote:
    article_upvotes.append(int(article.text.split()[0]))


index = article_upvotes.index(max(article_upvotes))
print(max(article_upvotes))
print(article_texts[index])
print(article_links[index])