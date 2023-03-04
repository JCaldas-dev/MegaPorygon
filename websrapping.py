# for link in links:
#     replay_url = "https://replay.pokemonshowdown.com" + link["href"] + ".log"
#     replay_response = requests.get(replay_url)
#     filename = "logs/" + link["href"][1:].replace("/", "_") + ".log"
#     with open(filename, "w") as f:
#         f.write(replay_response.text)

import time
import datetime
import os
import requests
from bs4 import BeautifulSoup

logs_folder = 'logs/' #'highrating/'
downloaded_replays = []
i=0
format = "/gen8ou-"

for filename in os.listdir(logs_folder):
    if filename.endswith('.log'):
        downloaded_replays.append(format+filename.replace(".log",""))
        i+=1
print("Current amount of logs "+str(i))    
        
while True:
    # Send a request to the page with battle replays
    response = requests.get("https://replay.pokemonshowdown.com/search/?format=gen8ou")
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the links to replay pages
    links = soup.select("a[href^='/']")

    # Loop through the links and download the replay if it hasn't been downloaded already
    for link in links:
        href = link.get("href")
        if href.startswith(format) and href not in downloaded_replays:
            i+=1
            print(datetime.datetime.now().strftime('%H:%M:%S')+" Found new replay not yet downloaded.")
            print("Current amount of logs "+str(i))
            # Download the replay
            replay_id = href.split("-")[-1].replace("/", "_")
            url = f"https://replay.pokemonshowdown.com/{href}.log"
            response = requests.get(url)
            replay_log = response.text

            # Save the replay to a file
            filename = logs_folder+replay_id+".log"
            with open(filename, "w") as f:
                f.write(replay_log)

            # Add the replay id to the list of downloaded replays
            downloaded_replays.append(href)

    # Wait for some time before checking for new replays
    time.sleep(10)
