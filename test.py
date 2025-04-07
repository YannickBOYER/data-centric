import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytrends.request import TrendReq
import pandas as pd
from collections import Counter
import time

# Keyworld : sneakers, crop top

# --- Configuration Spotify ---
# SPOTIFY_CLIENT_ID = 'a82b40077f194fc79e4c00733a8147e9'
# SPOTIFY_CLIENT_SECRET = '850986d246474907a940f6fe09ad928b'

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#     client_id=SPOTIFY_CLIENT_ID,
#     client_secret=SPOTIFY_CLIENT_SECRET
# ))

# --- Pytrends ---
pytrends = TrendReq(hl='en-US', tz=360, requests_args={'headers': {'User-Agent': 'Mozilla/5.0'}})

def get_top_countries_for_product(keyword):
    # pytrends.build_payload([keyword], timeframe='today 12-m', geo='')
    # trends = pytrends.interest_by_region()
    # trends = trends.sort_values(by=keyword, ascending=False)
    pytrends.build_payload([keyword], timeframe='today 12-m', geo='')
    time.sleep(5)  # éviter les 429
    trends = pytrends.interest_by_region()
    trends = trends.sort_values(by=keyword, ascending=False)
    return trends

# def get_top_tracks_by_country(country):
#     spotify_df = pd.read_csv('spotify_top_songs.csv')
#     return spotify_df.head


if __name__ == "__main__":
    #print(get_top_tracks_by_country("France"))
    print(get_top_countries_for_product("Macron"))


# def get_top_countries_for_product(keyword, top_n=5):
#     pytrends.build_payload([keyword], timeframe='today 12-m', geo='')
#     trends = pytrends.interest_by_region()
#     trends = trends.sort_values(by=keyword, ascending=False)
#     return trends.head(top_n)['geoName'].tolist()

# def get_top_tracks_for_country(country_code, limit=10):
#     try:
#         top_tracks = sp.country_top_tracks(country_code, limit=limit)
#     except:
#         top_tracks = sp.playlist_tracks(f'top-50-{country_code.lower()}')
#     return top_tracks['tracks']['items']

# def extract_genres_from_tracks(tracks):
#     artist_ids = list({artist['id'] for track in tracks for artist in track['track']['artists']})
#     genres = []
#     for i in range(0, len(artist_ids), 50):  # Spotify limite à 50 par appel
#         artists = sp.artists(artist_ids[i:i+50])['artists']
#         for artist in artists:
#             genres.extend(artist['genres'])
#     return genres

# def suggest_music_genres_for_product(product_keyword):
#     print(f"🔍 Analyse du produit : {product_keyword}")
#     countries = get_top_countries_for_product(product_keyword, top_n=5)
#     print(f"🌍 Pays où '{product_keyword}' est populaire : {countries}")

#     all_genres = []
#     for country in countries:
#         print(f"🎧 Récupération des titres populaires en {country}...")
#         try:
#             # Playlist des top 50
#             playlists = sp.search(f'top 50 {country}', type='playlist', limit=1)
#             if playlists['playlists']['items']:
#                 playlist_id = playlists['playlists']['items'][0]['id']
#                 tracks = sp.playlist_tracks(playlist_id)['items']
#                 genres = extract_genres_from_tracks(tracks)
#                 all_genres.extend(genres)
#         except Exception as e:
#             print(f"❌ Erreur pour {country} : {e}")
#             continue

#     # Compter les genres
#     genre_counts = Counter(all_genres)
#     top_genres = genre_counts.most_common(5)

#     print("\n🎯 Genres musicaux les plus pertinents pour ce produit :")
#     for genre, count in top_genres:
#         print(f"- {genre} ({count} occurrences)")

#     return top_genres

# Exemple
# if __name__ == "__main__":
#     suggest_music_genres_for_product("sneakers")
