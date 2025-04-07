import pandas as pd
import pycountry
from pytrends.request import TrendReq
import os
import music_functions as mf

pytrends = TrendReq(hl='en-US', tz=360, requests_args={'headers': {'User-Agent': 'Mozilla/5.0'}})
sp = mf.configure_spotify_dataset()

def find_dataset_by_product(product):
    try:
        if(os.path.exists(f'product-dataset/{product.lower()}.csv') == False):
            pytrends.build_payload([product], timeframe='today 12-m', geo='')
            trends = pytrends.interest_by_region()
            trends = trends.sort_values(by=product, ascending=False)
            df = pd.DataFrame(trends)
            df.to_csv(f'product-dataset/{product.lower()}.csv', index=False)
            return pd.read_csv(f'product-dataset/{product.lower()}.csv')
    except:
        print(f"Aucun dataset n'a été trouvé pour le produit : {product}")
        return []

def get_top_countries_for_product(product):
    if(os.path.exists(f'product-dataset/{product.lower()}.csv') == False):
        return find_dataset_by_product(product)
    else:
        return pd.read_csv(f'product-dataset/{product.lower()}.csv')

def get_top_tracks_by_country(country_code, limit):
    tracks = []
    popular_songs_in_country = sp[sp['country'] == country_code.upper()]
    for index, row in popular_songs_in_country.head(limit).iterrows():
        tracks.append({
            "rang_du_top": row["daily_rank"],
            "titre": row["name"],
            "artiste": row["artists"],
            "ambiance": mf.get_ambiance(row["mode"], row["valence"]),
            "energie": mf.get_energy(row["tempo"], row["energy"]),
            "contenu_explicite": mf.is_contenu_explicit(row["is_explicit"])
        })
    return tracks

def get_country_code(country_name):
    country = pycountry.countries.get(name=country_name)
    if country:
        return country.alpha_2
    else:
        return None

if __name__ == "__main__":
    # On récupère le produit cible
    product = input("Entrez le nom d'un produit : ")

    # On récupère la liste des pays ou le produit est le plus recherché
    top_countries_by_product = get_top_countries_for_product(product)

    if(len(top_countries_by_product) != 0):
        # On récupère le code alpha 2 du pays 
        # et on affiche les sons les plus écoutés du top streaming
        first_country = top_countries_by_product.index[1]
        print(f"Pays ciblé : {first_country}")
        country_code = get_country_code(first_country)
        df = pd.DataFrame(get_top_tracks_by_country(country_code, 50))
        
        df.to_json("musics.json", orient="records", force_ascii=False, indent=2)
        print("Analyse terminée, résultat générés dans le fichier musics.json")