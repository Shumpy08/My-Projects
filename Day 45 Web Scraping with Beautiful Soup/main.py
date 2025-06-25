import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
hacker_news = response.text
soup = BeautifulSoup(hacker_news, "html.parser")
article_tag = soup.findAll(name="a")
print(article_tag)
#
# with open(file="website.html", encoding="utf8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# print(soup.findAll("p"))
