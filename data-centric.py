import pandas as pd
import pycountry

import music_functions as mf
import trends_functions as tf

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
    top_countries_by_product = tf.get_top_countries_for_product(product)

    if(len(top_countries_by_product) != 0):
        first_country = top_countries_by_product.index[1]
        print(f"Pays ciblé : {first_country}")

        # On récupère le code alpha 2 du pays 
        country_code = get_country_code(first_country)
        df = pd.DataFrame(mf.get_top_tracks_by_country(country_code, 50))
        
        # On enregistre le résultat dans un fichier json
        df.to_json("musics.json", orient="records", force_ascii=False, indent=2)
        print("Analyse terminée, résultat générés dans le fichier musics.json")