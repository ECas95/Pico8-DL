import asyncio
import os
import logging
import aiohttp
import aiofiles
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s"
)

base_url = "https://www.lexaloffle.com/bbs/?cat=7&carts_tab=1&page={}&mode=carts"
base1 = "https://www.lexaloffle.com/bbs/"
base2 = "https://www.lexaloffle.com/"
MAX_CONCURRENT_REQUESTS = 10
FolderName = "Roms"


async def download_game(session, link, sem):
    try:
        async with sem:
            async with session.get(link) as response:
                soup = BeautifulSoup(await response.text(), "lxml")
                game_link = soup.find("a", {"href": lambda c: c and "/bbs/cposts/" in c})["href"]
                game_name = game_link.split("/")[-1]
                game_path = os.path.join(FolderName, game_name)
                async with session.get(base2 + game_link) as game_response:
                    async with aiofiles.open(game_path, "wb") as f:
                        async for data in game_response.content.iter_chunked(1024):
                            await f.write(data)
                logging.info(f"Successfully downloaded {game_name}")
    except Exception as e:
        logging.error(f"Error occurred while processing {link}: {str(e)}")


async def main():
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)
    sem = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
        links = set()
        for i in range(400):
            url = base_url.format(i)
            try:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), "lxml")
                    previews = soup.find_all("div", id=lambda x: x and x.startswith("pdat_"))
                    logging.info(f"Successfully retrieved HTML content from {url}")
                    for preview in previews:
                        thread_id = preview["id"].replace("pdat_", "")
                        thread_link = base1 + "?pid=" + thread_id + "#p"
                        links.add(thread_link)
            except Exception as e:
                logging.error(f"Error occurred while processing {url}: {str(e)}")

        tasks = []
        for i in range(0, len(links), MAX_CONCURRENT_REQUESTS):
            batch = list(links)[i:i+MAX_CONCURRENT_REQUESTS]
            tasks += [download_game(session, link, sem) for link in batch]

        try:
            await asyncio.gather(*tasks, return_exceptions=True)
        except asyncio.CancelledError:
            logging.warning("Asyncio event loop was closed before all tasks completed.")
            for task in tasks:
                if not task.done():
                    task.cancel()
        except Exception as e:
            logging.error(f"An error occurred during task execution: {str(e)}")
            for task in tasks:
                if not task.done():
                    task.cancel()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "Event loop is closed" not in str(e):
            raise e
        else:
            logging.warning("Asyncio event loop was closed before all tasks completed.")
