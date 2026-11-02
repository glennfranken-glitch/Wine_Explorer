import requests
import os
from dotenv import load_dotenv

# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("VINOFYI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
	print("API-sleutel ontbreekt.")
else:
	print("API-sleutel is succesvol geladen.")
base_url = 'https://vinofyi.com'

# API Endpoints
url_ls_flavors = base_url+'/api/v1/flavors/'
url_ls_grapes = base_url+'/api/v1/grapes/'
url_search = base_url+'/api/v1/search/'
url_wineries = base_url+'/api/v1/wineries/'
url_countries = base_url+'/api/v1/countries/'

def get_all_grapes():
    url = url_ls_grapes
    grapes_data = []

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        grapes_data.extend(data["results"])
        
        url = data["next"]

    return grapes_data

def get_all_flavors():
    url = url_ls_flavors
    flavors_data = []

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        flavors_data.extend(data["results"])
        
        url = data["next"]

    return flavors_data

def get_flavor_categories():
    """Haal alle unieke smaakcategorieën op uit de API."""
    url = url_ls_flavors
    categories = set()

    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        for flavor in data["results"]:
            categories.add(flavor["category"])

        url = data["next"]

    return sorted(categories)

def search_wineries(search_text):
    url = url_wineries+f"{search_text}/"
    response = requests.get(
        url
        )

    data = response.json()

    return data

def list_wineries():
    wineries = set()
    url = url_wineries
    response = requests.get(
        url
        )

    data = response.json()

    for winery in data["results"]:
        wineries.add(["name"])

    return wineries

def list_countries():
    countries = set()
    url = url_countries
    response = requests.get(
        url
        )