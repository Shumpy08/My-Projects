import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
movies = response.text
soup = BeautifulSoup(movies, "html.parser")
all_movies = soup.findAll(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
flims = (movie_titles[::-1])
print(flims)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in flims:
        file.write(f"{movie}\n")
