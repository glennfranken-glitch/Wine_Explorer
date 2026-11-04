import requests
import os
from dotenv import load_dotenv

MAX_PAGES = 5

# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("VINOFYI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
    raise ValueError("API_KEY ontbreekt in het .env-bestand.")
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
    """Haal maximaal vijf pagina's met druiven op uit de API."""
    url = url_ls_grapes
    grapes_data = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        response = requests.get(url, timeout=10)
        if response.status_code == 429:
            print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
            return []
        response.raise_for_status()

        data = response.json()
        grapes_data.extend(data["results"])

        url = data["next"]
        page_count += 1

    return grapes_data

def get_all_flavors():
    """Haal maximaal vijf pagina's met smaken op uit de API."""
    url = url_ls_flavors
    flavors_data = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        response = requests.get(url, timeout=10)
        if response.status_code == 429:
            print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
            return []
        response.raise_for_status()

        data = response.json()
        flavors_data.extend(data["results"])

        url = data["next"]
        page_count += 1

    return flavors_data

def get_flavor_categories():
    """Haal alle unieke smaakcategorieën op uit de API."""
    url = url_ls_flavors
    categories = set()

    while url:
        response = requests.get(url, timeout=10)
        if response.status_code == 429:
            print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
            return []
        response.raise_for_status()

        data = response.json()

        for flavor in data["results"]:
            categories.add(flavor["category"])

        url = data["next"]

    return sorted(categories)

def search_wineries(search_text):
    """Zoek wijnhuizen op basis van een zoekterm."""
    response = requests.get(
        url_search,
        params={"q": search_text},
        timeout=10
    )

    if response.status_code == 429:
        print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
        return []

    response.raise_for_status()

    data = response.json()

    wineries = [
        result for result in data["results"]
        if result["type"] == "winery"
    ]

    return wineries

def list_wineries():
    """Haal maximaal vijf pagina's met wijnhuizen op uit de API."""
    url = url_wineries
    wineries = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        response = requests.get(url, timeout=10)
        if response.status_code == 429:
            print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
            return []
        response.raise_for_status()

        data = response.json()
        wineries.extend(data["results"])

        url = data["next"]
        page_count += 1

    return wineries

def get_winery_details(winery):
    """Haalt de details van een wijnhuis op."""

    url = base_url + f"/api/winery/{winery['slug']}/"

    response = requests.get(url, timeout=10)

    if response.status_code == 429:
        print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
        return None

    response.raise_for_status()

    return response.json()

def list_countries():
    countries = set()
    url = url_countries
    response = requests.get(
        url
        )
    if response.status_code == 429:
        print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
        return []
    data = response.json()

    return data

def view_country(country):
    url = url_countries
    response = requests.get(
        url+f"{country}/"
        )
    if response.status_code == 429:
        print("Vinofyi heeft tijdelijk te veel verzoeken ontvangen.")
        return []
    data = response.json()

    return data