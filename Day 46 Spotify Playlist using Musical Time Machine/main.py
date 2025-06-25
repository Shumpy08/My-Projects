# import requests
# from bs4 import BeautifulSoup
# url = "https://www.billboard.com/charts/hot-100/2018-02-03/"
# date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: F")
# response = requests.get(url=f"{url}{date}")
# soup = BeautifulSoup(response.text, "html.parser")
# song_details = soup.findAll(name="li", class_="lrv-u-width-100p")
# song_title = [song.find(name="h3") for song in song_details]
# print(song_title)
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
# response.raise_for_status()
# data = response.text
#
# soup = BeautifulSoup(data, "html.parser")
#
# song = []
#
# tag_list = soup.select(selector="li h3")
# for tag in tag_list:
#     if tag["id"] == "title-of-a-story":
#         name = tag.getText()
#         song.append(name.replace("\n", "").replace("\t", ""))
# print(song)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:9000/callback",
        client_id="016ea0d776ff4acc8c49c645bd308c08",
        client_secret="32d4cba3fd46477a81de91846cdea556",
        show_dialog=True,
        cache_path="token.txt",
        username="shumpy",
    )
)
user_id = sp.current_user()["id"]
print(user_id)