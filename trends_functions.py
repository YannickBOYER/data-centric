import os
from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360, requests_args={'headers': {'User-Agent': 'Mozilla/5.0'}})

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