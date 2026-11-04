import requests
import os
from dotenv import load_dotenv

# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("WINEAPI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
	print("API-sleutel ontbreekt.")
else:
	print("API-sleutel is succesvol geladen.")
base_url = 'https://api.wineapi.io'

# API Endpoints
url_wine_search=base_url+'/wines/search'

def search_wine(wine):
    url = url_wine_search
    response = requests.get(
        url,
        headers={
          "X-API-Key": api_key
        },
        params={
          "q": f"{wine}",
          "limit": "20",
          "offset": "0"
        }
    )
    response.raise_for_status()

    data = response.json()

    return data
    