import pandas as pd

def configure_spotify_dataset():
    sp = pd.read_csv('spotify_top_songs.csv')
    return sp.drop_duplicates(subset=['name', 'artists', 'country'])

sp = configure_spotify_dataset()

def get_ambiance(mode, valence):
    ambiance = ""
    if(valence > 0.7):
        ambiance = "Musique Joyeuse"
    elif (valence < 0.3):
        ambiance = "Musique triste"
    else:
        if(mode == 1):
            ambiance = f"Musique à tendance ouverte"
        else:
            ambiance = f"Musique à tendance profonde"
    return ambiance

def get_energy(tempo, energy_value):
    if(tempo >= 120 and energy_value > 0.5):
        return "Energétique"
    else:
        return "Calme"
    
def is_contenu_explicit(is_explicit):
    if(is_explicit):
        return "Oui"
    else:
        return "Non"
    
def get_top_tracks_by_country(country_code, limit):
    tracks = []
    popular_songs_in_country = sp[sp['country'] == country_code.upper()]
    for index, row in popular_songs_in_country.head(limit).iterrows():
        tracks.append({
            "rang_du_top": row["daily_rank"],
            "titre": row["name"],
            "artiste": row["artists"],
            "ambiance": get_ambiance(row["mode"], row["valence"]),
            "energie": get_energy(row["tempo"], row["energy"]),
            "contenu_explicite": is_contenu_explicit(row["is_explicit"])
        })
    return tracks