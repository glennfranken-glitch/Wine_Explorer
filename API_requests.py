import requests

from logger import get_logger

logger = get_logger("api_requests")


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
        logger.error("Timeout bij API-request: %s", url)
        print("De API reageert niet op tijd.")
        raise

    except requests.exceptions.ConnectionError:
        logger.error("Verbindingsfout bij API-request: %s", url)
        print("Er kon geen verbinding worden gemaakt met de API.")
        raise

    except requests.exceptions.HTTPError as error:
        logger.error(
            "HTTP-fout bij API-request naar %s: %s",
            url,
            error
        )
        print(f"De API heeft een HTTP-fout teruggegeven: {error}")
        raise

    except requests.exceptions.JSONDecodeError:
        logger.error("Ongeldige JSON-response van API: %s", url)
        print("De API heeft geen geldige JSON-response teruggegeven.")
        raise

    except requests.exceptions.RequestException as error:
        logger.error(
            "Onverwachte requestfout bij %s: %s",
            url,
            error
        )
        print(f"Er is een fout opgetreden bij de API-request: {error}")
        raise
