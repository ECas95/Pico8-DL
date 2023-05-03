import os
import requests
from bs4 import BeautifulSoup

base_url = "https://www.lexaloffle.com/bbs/?cat=7&carts_tab=1&page={}&mode=carts"
base1 = "https://www.lexaloffle.com/bbs/"
base2 = "https://www.lexaloffle.com/"

# Create a new directory to store the games
if not os.path.exists("Roms"):
    os.mkdir("Roms")

links = []
for i in range(50):
    url = base_url.format(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    carts = soup.find_all("div", {"id": lambda c: c and "pdat" in c})
    for cart in carts:
        link = cart.find("a")["href"]
        link = link.replace("tid", "pid")
        links.append(base1+link)

for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    game = soup.find("a", {"href": lambda c: c and "/bbs/cposts/" in c})
    if game:
        game_link = game['href']
        game_name = game_link.split("/")[-1]
        game_path = os.path.join("Roms", game_name)
        response = requests.get(base2+game_link)
        with open(game_path, "wb") as f:
            f.write(response.content)
        print("Downloaded", game_name)
