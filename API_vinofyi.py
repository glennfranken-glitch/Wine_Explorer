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
    """
    Haalt maximaal vijf pagina's met druiven op uit de Vinofyi API.

    Output:
        Een lijst met druiven.
    """

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
    """
    Haalt maximaal vijf pagina's met smaken op uit de Vinofyi API.

    Output:
        Een lijst met smaken.
    """

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
    """
    Haalt de unieke smaakcategorieën op uit de Vinofyi API.

    Output:
        Een gesorteerde lijst met smaakcategorieën.
    """

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
    """
    Zoekt wijnhuizen op basis van een zoekterm.

    Input:
        search_text = zoekterm voor het wijnhuis

    Output:
        Een lijst met gevonden wijnhuizen.
    """

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
    """
    Haalt maximaal vijf pagina's met smaken op uit de Vinofyi API.

    Output:
        Een lijst met smaken.
    """

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
    """
    Haalt de details van een geselecteerd wijnhuis op.

    Input:
        winery = dictionary met gegevens van het wijnhuis

    Output:
        Een dictionary met de details van het wijnhuis.
    """

    url = base_url + f"/api/winery/{winery['slug']}/"

    data = API_requests.make_api_request(url)

    return data

def get_all_wines():
    """
    Haalt maximaal vijf pagina's met wijnen op uit de Vinofyi API.

    Output:
        Een lijst met wijnen.
    """

    url = url_ls_wines
    wines_data = []
    page_count = 0

    while url and page_count < MAX_PAGES:
        data = API_requests.make_api_request(url)

        wines_data.extend(data["results"])

        url = data["next"]
        page_count += 1

    return wines_data

def search_wines(search_text):
    """
    Zoekt wijnen op basis van een zoekterm.

    Input:
        search_text = zoekterm voor de wijn

    Output:
        Een lijst met gevonden wijnen.
    """

    data = API_requests.make_api_request(
        url_search,
        params={"q": search_text}
    )

    wines = [
        result for result in data["results"]
        if result["type"] == "wine"
    ]

    return wines

def get_wine_details(slug):
    """
    Haalt maximaal vijf pagina's met smaken op uit de Vinofyi API.

    Output:
        Een lijst met smaken.
    """

    url = base_url + f"/api/wine/{slug}/"

    data = API_requests.make_api_request(url)

    return data

def list_countries():
    """
    Haalt de beschikbare landen op uit de Vinofyi API.

    Output:
        De response met beschikbare landen.
    """

    data = API_requests.make_api_request(url_countries)

    return data

def view_country(country):
    """
    Haalt maximaal vijf pagina's met smaken op uit de Vinofyi API.

    Output:
        Een lijst met smaken.
    """

    url = url_countries + f"{country}/"

    data = API_requests.make_api_request(url)

    return data

def list_regions(country=None):
    """
    Haalt regio's op en filtert deze eventueel op land.

    Input:
        country = optionele landnaam waarop gefilterd wordt

    Output:
        Een lijst met regio's.
    """

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