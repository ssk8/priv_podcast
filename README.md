# priv_podcast

host private podcasts on local server

clone repo, make a directory "assets" and add a logo.jpg and mp3 files.

run autopodgen to generate the xml/rss file and then host it by starting a server

for python server:

python -m http.server 8000 -d assets 

get.py is for downloading mp3s from google drive
