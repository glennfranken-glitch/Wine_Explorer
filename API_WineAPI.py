import os

from dotenv import load_dotenv

import API_requests


# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("WINEAPI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
    raise ValueError("WINEAPI_API_KEY ontbreekt in het .env-bestand.")

base_url = 'https://api.wineapi.io'

# API Endpoints
url_wine_search = base_url + '/wines/search'


def search_wine(wine):
    """
    Zoekt wijnen op basis van een zoekterm via de WineAPI.

    Input:
        wine = zoekterm voor de wijn

    Output:
        De JSON-response met de gevonden wijnen.
    """

    data = API_requests.make_api_request(
        url_wine_search,
        params={
            "q": wine,
            "limit": 20,
            "offset": 0
        },
        headers={
            "X-API-Key": api_key
        }
    )

    return data