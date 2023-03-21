from bs4 import BeautifulSoup
import requests
import os

CLASS = os.environ["CLASS"]
BILLBOARD_SITE = os.environ["BILLBOARD_SITE"]

date = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
response = requests.get(BILLBOARD_SITE + date)
web_archive = response.text
soup = BeautifulSoup(web_archive, "html.parser")


songs = soup.find_all(class_=CLASS)
titles = []
for song in songs:
    title = song.find(name="h3").getText().replace("\n", "").replace("\t", "")
    titles.append(title)

print(titles)
with open("songs.txt", "wt") as file:
    file.write(date + "\n")
for title in titles:
    with open("songs.txt", "at") as file:
        file.write(title + '\n')


