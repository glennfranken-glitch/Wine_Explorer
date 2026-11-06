import os
from dotenv import load_dotenv
import API_requests

MAX_PAGES = 5

# Laad de variabelen uit .env
load_dotenv()

# Lees de API-sleutel uit
api_key = os.getenv("VINOFYI_API_KEY")

# Controleer of de sleutel aanwezig is
if api_key is None:
    raise ValueError("API_KEY ontbreekt in het .env-bestand.")

base_url = 'https://vinofyi.com'

# API Endpoints
url_ls_flavors = base_url+'/api/v1/flavors/'
url_ls_grapes = base_url+'/api/v1/grapes/'
url_search = base_url+'/api/v1/search/'
url_wineries = base_url+'/api/v1/wineries/'
url_countries = base_url+'/api/v1/countries/'
url_regions = base_url+"/api/v1/regions/"
url_ls_wines = base_url+"/api/v1/wines/"

def get_all_grapes():
    """Haal maximaal vijf pagina's met druiven op uit de API."""

    url = url_ls_grapes
    grapes_data = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

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
        data = API_requests.make_api_request(url)

        flavors_data.extend(data["results"])

        url = data["next"]
        page_count += 1

    return flavors_data

def get_flavor_categories():
    """Haal alle unieke smaakcategorieën op uit de API."""

    url = url_ls_flavors
    categories = set()
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

        for flavor in data["results"]:
            categories.add(flavor["category"])

        url = data["next"]
        page_count += 1

    return sorted(categories)

def search_wineries(search_text):
    """Zoek wijnhuizen op basis van een zoekterm."""

    data = API_requests.make_api_request(
        url_search,
        params={"q": search_text}
    )

    wineries = [
        result for result in data["results"]
        if result["type"] == "winery"
    ]

    return wineries

def list_wineries(country=None):
    """Haal wijnhuizen op, eventueel gefilterd op land."""

    url = url_wineries
    wineries = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

        wineries.extend(data["results"])

        url = data["next"]
        page_count += 1

    if country:
        wineries = [
            winery for winery in wineries
            if winery["country_name"].lower() == country.lower()
        ]

    return wineries

def get_winery_details(winery):
    """Haalt de details van een wijnhuis op."""

    url = base_url + f"/api/winery/{winery['slug']}/"

    data = API_requests.make_api_request(url)

    return data

def get_all_wines():
    """Haalt maximaal vijf pagina's met wijnen op uit de API."""

    url = url_ls_wines
    wines_data = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

        wines_data.extend(data["results"])

        url = data["next"]
        page_count += 1

    return wines_data

def get_wine_details(slug):
    """Haalt de details van een wijn op."""

    url = base_url + f"/api/wine/{slug}/"

    data = API_requests.make_api_request(url)

    return data

def list_countries():
    """Haalt de beschikbare landen op uit de API."""

    data = API_requests.make_api_request(url_countries)

    return data

def view_country(country):
    """Haalt de gegevens van een specifiek land op."""

    url = url_countries + f"{country}/"

    data = API_requests.make_api_request(url)

    return data

def list_regions(country=None):
    """Haalt regio's op, eventueel gefilterd op land."""

    url = url_regions
    regions = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

        regions.extend(data["results"])

        url = data["next"]
        page_count += 1

    if country:
        regions = [
            region for region in regions
            if region["country_name"].lower() == country.lower()
        ]

    return regions