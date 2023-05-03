import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

base_url = "https://www.lexaloffle.com/bbs/?cat=7&carts_tab=1&page={}&mode=carts"
base1 = "https://www.lexaloffle.com/bbs/"
base2 = "https://www.lexaloffle.com/"

# Create a new directory to store the games
if not os.path.exists("Roms"):
    os.mkdir("Roms")

# Create a requests session and enable connection pooling
session = requests.Session()
session.keep_alive = True
session.adapters.max_retries = 3
session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=1000, max_retries=3))

links = []
for i in range(50):
    url = base_url.format(i)
    response = session.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    carts = soup.find_all("div", {"id": lambda c: c and "pdat" in c})
    for cart in carts:
        link = cart.find("a")["href"]
        link = link.replace("tid", "pid")
        links.append(base1+link)

def download_game(link):
    response = session.get(link)
    soup = BeautifulSoup(response.content, "lxml")
    game = soup.find("a", {"href": lambda c: c and "/bbs/cposts/" in c})
    if game:
        game_link = game['href']
        game_name = game_link.split("/")[-1]
        game_path = os.path.join("Roms", game_name)
        response = session.get(base2+game_link)
        with open(game_path, "wb") as f:
            f.write(response.content)
        print("Downloaded", game_name)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(download_game, links)
