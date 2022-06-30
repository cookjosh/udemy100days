# Day 46 Project - Billboard Top 100 Spotify Playlist
# Then use Spotify API to build a playlist of those songs

import os
import re
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# --- Spotify auth flow --- #
spotify_id = os.environ.get("SPOTIPY_CLIENT_ID")
spotify_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
spotify_redirect_uri="http://example.com"

auth_manager = SpotifyOAuth(client_id=spotify_id, client_secret=spotify_secret, redirect_uri=spotify_redirect_uri, scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=auth_manager)

# --- Billboard website scrape for top 100 songs from given date --- #
user_date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}/")

soup = BeautifulSoup(response.text, "html.parser")
big_soup = soup.find_all(name="li", class_="o-chart-results-list__item")

# Create list of titles parsing quotes and spaces out
title_list = []
spacer = re.compile(r'(\S)([A-Z])')
for soup in big_soup:
    if soup.h3:
        title = "".join((soup.h3.text).split())
        title = re.sub(spacer, r"\1 \2", title)
        title_list.append(title)


# --- Spotify - create playlist and add songs from Billboard list --- #
spotify_user_id = (sp.current_user())["id"]

# Grab all track URNs from Spotify Web API and create list
# Pass on tracks that don't return a result in the search
spotify_uri_list = []
for title in title_list:
    try:
        spotify_uri_list.append((sp.search(title))["tracks"]["items"][0]["uri"])
    except:
        pass
print(spotify_uri_list)

# Create new playlist
# Add tracks from Billboard scrape Spotify search results to playlist
create_playlist = sp.user_playlist_create(user=spotify_user_id, name=f"{user_date} Billboard 100", public="false")
sp.user_playlist_add_tracks(user=spotify_user_id, playlist_id=create_playlist["id"], tracks=spotify_uri_list)

