import Menus
import API_vinofyi
import json
from datetime import date
from pathlib import Path

from logger import get_logger

logger = get_logger("tasting_notes")

TASTING_NOTES_FILE = Path(__file__).resolve().parent / "tasting_notes.json"


def load_tasting_notes():
    """
    Leest alle opgeslagen proefnotities uit het JSON-bestand.

    Output:
        Een lijst met proefnotities.
        Als het bestand nog niet bestaat, wordt een lege lijst teruggegeven.
    """

    if not TASTING_NOTES_FILE.exists():
        return []

    try:
        with open(TASTING_NOTES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (OSError, json.JSONDecodeError):
        logger.exception(
            "Fout bij het lezen van proefnotities uit %s",
            TASTING_NOTES_FILE
        )
        raise



def save_tasting_notes(tasting_notes):
    """
    Slaat alle proefnotities op in het JSON-bestand.

    Input:
        tasting_notes = lijst met proefnotities
    """

    try:
        with open(TASTING_NOTES_FILE, "w", encoding="utf-8") as file:
            json.dump(tasting_notes, file, indent=4, ensure_ascii=False)

    except (OSError, TypeError, ValueError):
        logger.exception(
            "Fout bij het opslaan van proefnotities in %s",
            TASTING_NOTES_FILE
        )
        raise

def select_wine():
    """
    Allows the user to search for and select a wine.
    If no wine is found, the user can enter a custom wine name.

    Output:
        Returns the selected wine or None.
    """

    search_term = Menus.menu_search_wine()

    if not search_term:
        return None

    wines = API_vinofyi.search_wines(search_term)

    if not wines:
        print("Geen wijnen gevonden.")

        choice = Menus.menu_select_option(
            "Wil je zelf een wijnnaam invoeren?",
            ["Ja", "Nee"]
        )

        if choice != "Ja":
            return None

        wine_name = input("Naam van de wijn: ").strip()

        if not wine_name:
            print("Er is geen wijnnaam ingevoerd.")
            return None

        return {
            "source": "custom",
            "slug": None,
            "name": wine_name,
            "winery": {},
            "vintage": None
        }

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

def record_aroma():
    """
    Asks the user questions about the wine's aroma.

    Output:
        Returns a dictionary with the aroma observations.
    """

    aroma = {}

    aroma["intensity"] = Menus.menu_select_option(
        "Hoe intens is de geur?",
        [
            "Licht",
            "Gemiddeld",
            "Intens"
        ]
    )

    if aroma["intensity"] is None:
        return None

    aroma["aromas"] = Menus.menu_select_aromas()

    return aroma

def record_taste():
    """
    Asks the user questions about the wine's taste.

    Output:
        Returns a dictionary with the taste observations.
    """

    taste = {}

    taste["acidity"] = Menus.menu_select_option(
        "Hoe ervaar je de zuren?",
        ["Laag", "Gemiddeld", "Hoog"]
    )

    if taste["acidity"] is None:
        return None

    taste["sweetness"] = Menus.menu_select_option(
        "Hoe zoet of droog is de wijn?",
        [
            "Beendroog",
            "Droog",
            "Off-dry",
            "Halfzoet",
            "Zoet",
            "Zeer zoet"
        ]
    )

    if taste["sweetness"] is None:
        return None

    taste["body"] = Menus.menu_select_option(
        "Hoe ervaar je de body?",
        ["Licht", "Gemiddeld", "Vol"]
    )

    if taste["body"] is None:
        return None

    taste["tannins"] = Menus.menu_select_option(
        "Hoe ervaar je de tannines?",
        ["Laag", "Gemiddeld", "Hoog", "Niet van toepassing"]
    )

    if taste["tannins"] is None:
        return None

    taste["aroma_match"] = Menus.menu_select_option(
        "Komen de smaken overeen met wat je rook?",
        ["Ja", "Gedeeltelijk", "Nee"]
    )

    if taste["aroma_match"] is None:
        return None

    return taste

def record_conclusion():
    """
    Asks the user questions about the wine and records their opinion.

    Output:
        Returns a dictionary with the conclusion.
    """

    conclusion = {}

    conclusion["finish"] = Menus.menu_select_option(
        "Hoe lang blijft de smaak hangen?",
        ["Kort", "Gemiddeld", "Lang"]
    )

    if conclusion["finish"] is None:
        return None

    conclusion["balance"] = Menus.menu_select_option(
        "Is de wijn in balans?",
        [
            "Uit balans",
            "Redelijk in balans",
            "Goed in balans"
        ]
    )

    if conclusion["balance"] is None:
        return None

    conclusion["liked"] = Menus.menu_select_option(
        "Vond je de wijn lekker?",
        ["Ja", "Nee", "Twijfel"]
    )

    if conclusion["liked"] is None:
        return None

    conclusion["reason"] = input(
        "\nWaarom wel of niet? "
    ).strip()

    return conclusion

def create_tasting_note():
    """
    Creates and saves a tasting note for a selected wine.

    Output:
        Saves the completed tasting note to the JSON file.
    """

    wine = select_wine()

    if wine is None:
        return None

    appearance = record_appearance()

    if appearance is None:
        return None

    aroma = record_aroma()

    if aroma is None:
        return None

    taste = record_taste()

    if taste is None:
        return None

    conclusion = record_conclusion()

    if conclusion is None:
        return None

    tasting_notes = load_tasting_notes()

    tasting_note = {
        "id": max(
            (note["id"] for note in tasting_notes),
            default=0
        ) + 1,
        "date": date.today().isoformat(),
        "wine": {
            "source": wine.get("source", "vinofyi"),
            "slug": wine.get("slug"),
            "name": wine.get("name"),
            "winery": (
                wine.get("winery") or {}
            ).get("name"),
            "vintage": wine.get("vintage")
        },
        "appearance": appearance,
        "aroma": aroma,
        "taste": taste,
        "conclusion": conclusion
    }

    tasting_notes.append(tasting_note)

    save_tasting_notes(tasting_notes)

    print("\nJe proefnotitie is opgeslagen!")

    return tasting_note

def show_tasting_notes():
    """
    Loads and displays saved tasting notes.

    Output:
        Displays the selected tasting note.
    """

    tasting_notes = load_tasting_notes()

    if not tasting_notes:
        print("Er zijn nog geen proefnotities opgeslagen.")
        return

    selected_note = Menus.menu_tasting_notes(tasting_notes)

    if selected_note is None:
        return

    Menus.show_tasting_note_details(selected_note)

def edit_tasting_note():
    """
    Allows the user to edit an existing tasting note.

    The user selects which section to update.

    Output:
        Saves the updated tasting note.
    """

    tasting_notes = load_tasting_notes()

    if not tasting_notes:
        print("Er zijn nog geen proefnotities opgeslagen.")
        return

    selected_note = Menus.menu_tasting_notes(tasting_notes)

    if selected_note is None:
        return

    section = Menus.menu_select_option(
        "Welk onderdeel wil je aanpassen?",
        [
            "Kijken - Uiterlijk",
            "Ruiken - Geur",
            "Proeven - Smaak",
            "Conclusie - Oordeel"
        ]
    )

    if section is None:
        return

    if section == "Kijken - Uiterlijk":
        updated_data = record_appearance()
        section_key = "appearance"

    elif section == "Ruiken - Geur":
        updated_data = record_aroma()
        section_key = "aroma"

    elif section == "Proeven - Smaak":
        updated_data = record_taste()
        section_key = "taste"

    else:
        updated_data = record_conclusion()
        section_key = "conclusion"

    if updated_data is None:
        return

    selected_note[section_key] = updated_data

    save_tasting_notes(tasting_notes)

    print("\nJe proefnotitie is bijgewerkt!")

def delete_tasting_note():
    """
    Allows the user to delete an existing tasting note.

    Output:
        Removes the selected tasting note from the JSON file.
    """

    tasting_notes = load_tasting_notes()

    if not tasting_notes:
        print("Er zijn nog geen proefnotities opgeslagen.")
        return

    selected_note = Menus.menu_tasting_notes(tasting_notes)

    if selected_note is None:
        return

    confirmation = Menus.menu_select_option(
        f"Weet je zeker dat je de proefnotitie "
        f"van {selected_note['wine']['name']} wilt verwijderen?",
        ["Ja, verwijderen", "Nee, annuleren"]
    )

    if confirmation != "Ja, verwijderen":
        print("Verwijderen geannuleerd.")
        return

    tasting_notes.remove(selected_note)

    save_tasting_notes(tasting_notes)

    print("De proefnotitie is verwijderd.")