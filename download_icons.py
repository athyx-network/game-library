import os
import time
import requests
from duckduckgo_search import DDGS

games = [
    ("Buckshot Roulette game icon png", "buckshot_roulette.png"),
    ("Five Nights at Freddy's 3 game icon png", "fnaf3.png"),
    ("Five Nights at Freddy's 4 game icon png", "fnaf4.png"),
    ("Happy Wheels game icon png", "happy_wheels.png"),
    ("Ragdoll Archers game icon png", "ragdoll_archers.png"),
    ("Undertale Last Breath game icon png", "undertale_last_breath.png")
]

dest_dir = "/home/bot/Desktop/gamelib/icons"
os.makedirs(dest_dir, exist_ok=True)

def download_image(url, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
    return False

with DDGS() as ddgs:
    for query, filename in games:
        print(f"Searching for {query}...")
        try:
            results = list(ddgs.images(query, max_results=5))
            success = False
            for res in results:
                url = res['image']
                print(f"Trying {url}...")
                if download_image(url, os.path.join(dest_dir, filename)):
                    print(f"Successfully downloaded {filename}")
                    success = True
                    break
            if not success:
                print(f"Could not download any image for {filename}")
        except Exception as e:
            print(f"Error searching for {query}: {e}")
        time.sleep(2)
