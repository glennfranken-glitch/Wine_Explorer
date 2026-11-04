import requests
import os
from dotenv import load_dotenv

# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("WINEAPI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
    raise ValueError("API_KEY ontbreekt in het .env-bestand.")
else:
	print("API-sleutel is succesvol geladen.")
base_url = 'https://api.wineapi.io'

# API Endpoints
url_wine_search=base_url+'/wines/search'

def search_wine(wine):
    """Zoek wijnen op basis van een zoekterm."""
    response = requests.get(
        url_wine_search,
        headers={
            "X-API-Key": api_key
        },
        params={
            "q": wine,
            "limit": 20,
            "offset": 0
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    data = search_wine("Chardonnay")

    for wine in data["results"]:
        print(wine["name"])