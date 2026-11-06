import requests

def make_api_request(url, params=None, headers=None, timeout=10):
    """
    Stuurt een GET-request naar een API-endpoint.

    Input:
        url = API-endpoint
        params = optionele queryparameters
        headers = optionele HTTP-headers
        timeout = maximale duur van de aanvraag in seconden

    Output:
        Geeft de API-response terug als JSON.
    """

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=timeout
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("De API reageert niet op tijd.")
        raise

    except requests.exceptions.ConnectionError:
        print("Er kon geen verbinding worden gemaakt met de API.")
        raise

    except requests.exceptions.HTTPError as error:
        print(f"De API heeft een HTTP-fout teruggegeven: {error}")
        raise

    except requests.exceptions.JSONDecodeError:
        print("De API heeft geen geldige JSON-response teruggegeven.")
        raise

    except requests.exceptions.RequestException as error:
        print(f"Er is een fout opgetreden bij de API-request: {error}")
        raise