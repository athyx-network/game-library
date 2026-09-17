import urllib.request
import json
import urllib.parse
import os

games = [
    ("Buckshot Roulette", "buckshot_roulette.png"),
    ("Five Nights at Freddy's 3", "fnaf3.png"),
    ("Five Nights at Freddy's 4", "fnaf4.png"),
    ("Happy Wheels", "happy_wheels.png"),
    ("Ragdoll Archers", "ragdoll_archers.png"),
    ("Undertale Last Breath", "undertale_last_breath.png")
]

dest_dir = "/home/bot/Desktop/gamelib/icons"
os.makedirs(dest_dir, exist_ok=True)

# Some hardcoded fallbacks just in case
fallbacks = {
    "Ragdoll Archers": "https://img.poki.com/cdn-cgi/image/quality=78,width=600,height=600,fit=cover,f=auto/b800c14c5b3d68df840fcc40bc64dc78.png",
    "Undertale Last Breath": "https://m.gjcdn.net/game-header/1000/944208-d6wms5c6-v4.jpg"
}

for game, filename in games:
    downloaded = False
    
    # Try Steam
    try:
        url = f"https://store.steampowered.com/api/storesearch/?term={urllib.parse.quote(game)}&l=english&cc=US"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        if data.get('total', 0) > 0:
            img_url = f"https://steamcdn-a.akamaihd.net/steam/apps/{data['items'][0]['id']}/header.jpg"
            urllib.request.urlretrieve(img_url, os.path.join(dest_dir, filename))
            print(f"Downloaded {game} from Steam")
            downloaded = True
            continue
    except Exception as e:
        pass

    # Try iTunes
    try:
        url = f"https://itunes.apple.com/search?term={urllib.parse.quote(game)}&entity=software"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        if data.get('resultCount', 0) > 0:
            img_url = data['results'][0]['artworkUrl512']
            urllib.request.urlretrieve(img_url, os.path.join(dest_dir, filename))
            print(f"Downloaded {game} from iTunes")
            downloaded = True
            continue
    except Exception as e:
        pass

    if game in fallbacks:
        try:
            req = urllib.request.Request(fallbacks[game], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(os.path.join(dest_dir, filename), 'wb') as out_file:
                out_file.write(response.read())
            print(f"Downloaded {game} from Fallback")
            downloaded = True
            continue
        except Exception as e:
            pass

    if not downloaded:
        print(f"Could not download {game}")
