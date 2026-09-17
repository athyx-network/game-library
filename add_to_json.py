import json
import os

games_file = "/home/bot/Desktop/gamelib/games.json"

with open(games_file, 'r') as f:
    games = json.load(f)

new_games = [
    {
        "name": "Buckshot Roulette",
        "path": "Buckshot Roulette.html",
        "icon": "icons/buckshot_roulette.png"
    },
    {
        "name": "Five Nights at Freddy's 3",
        "path": "Five Nights At Freddys 3.html",
        "icon": "icons/fnaf3.png"
    },
    {
        "name": "Five Nights at Freddy's 4",
        "path": "Five Nights At Freddys 4.html",
        "icon": "icons/fnaf4.png"
    },
    {
        "name": "Happy Wheels",
        "path": "Happy Wheels.html",
        "icon": "icons/happy_wheels.png"
    },
    {
        "name": "Ragdoll Archers",
        "path": "Ragdoll Archers.html",
        "icon": "icons/ragdoll_archers.png"
    },
    {
        "name": "Undertale: Last Breath",
        "path": "Undertale: Last Breath.html",
        "icon": "icons/undertale_last_breath.png"
    }
]

# Check for existing to avoid duplicates
existing_paths = set(g.get("path") for g in games)

added = False
for g in new_games:
    if g["path"] not in existing_paths:
        games.append(g)
        added = True

if added:
    with open(games_file, 'w') as f:
        json.dump(games, f, indent=2)
    print("Updated games.json successfully.")
else:
    print("No new games added.")
