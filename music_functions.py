import pandas as pd

def configure_spotify_dataset():
    sp = pd.read_csv('spotify_top_songs.csv')
    return sp.drop_duplicates(subset=['name', 'artists', 'country'])

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