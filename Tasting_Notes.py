import Menus
import API_vinofyi
import json
from pathlib import Path

TASTING_NOTES_FILE = Path(__file__).resolve().parent / "tasting_notes.json"

def load_tasting_notes():
    """
    Leest alle opgeslagen proefnotities uit het JSON-bestand.

    Output:
        Een lijst met proefnotities.
        Als het bestand nog niet bestaat, wordt een lege lijst teruggegeven.
    """

    if TASTING_NOTES_FILE.exists():
        with open(TASTING_NOTES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []

def save_tasting_notes(tasting_notes):
    """
    Slaat alle proefnotities op in het JSON-bestand.

    Input:
        tasting_notes = lijst met proefnotities
    """

    with open(TASTING_NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(tasting_notes, file, indent=4, ensure_ascii=False)

def select_wine():
    """
    Allows the user to search for and select a wine.

    Output:
        Returns the selected wine with its full details,
        or None if no wine is selected.
    """

    search_term = Menus.menu_search_wine()

    if not search_term:
        return None

    wines = API_vinofyi.search_wines(search_term)

    if not wines:
        print("Geen wijnen gevonden.")
        return None

    selected_wine = Menus.menu_wine_results(wines)

    if selected_wine is None:
        return None

    wine_details = API_vinofyi.get_wine_details(
        selected_wine["slug"]
    )

    return wine_details

def record_appearance():
    """
    Asks the user questions about the wine's appearance.

    Output:
        Returns a dictionary with the appearance observations.
    """

    appearance = {}

    appearance["color"] = Menus.menu_select_option(
        "Welke kleur heeft de wijn?",
        [
            "Strogeel",
            "Goudgeel",
            "Zalmroze",
            "Lichtroze",
            "Robijnrood",
            "Granaatrood",
            "Paarsrood",
            "Anders"
        ]
    )

    if appearance["color"] is None:
        return None

    appearance["clarity"] = Menus.menu_select_option(
        "Is de wijn helder of troebel?",
        [
            "Helder",
            "Licht troebel",
            "Troebel"
        ]
    )

    if appearance["clarity"] is None:
        return None

    return appearance

