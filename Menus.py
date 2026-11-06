from rich.console import Console
from rich.panel import Panel
from rich.console import Group
from rich.align import Align
from rich.table import Table
import API_vinofyi

flavors_data = None
grapes_data = None

console = Console()

def default_panel(text):
    """
    Maakt een standaard Wine Explorer panel.

    Input:
        text: text to display

    Output:
        panel: panel kan geprint worden middels console.print(panel)
    """
    panel = Panel(
    text,
    title= "[bold #722F37]🍷 Wine Explorer[/]",
    border_style="bold #D4AF37",
    style="#F4EBDD",
    padding=(1, 4)
              )

    return panel

def show_welcome_screen():
    """
    Display the welcome screen.

    Input:
        None

    Output:
        None
    """

    welcome_text = Group(
        "[bold #D4AF37]Welkom bij Wine Explorer![/]",
    "",
    "[#722F37]Leuk dat je met ons meegaat op[/]",
    "[#722F37]ontdekkingsreis door de wereld van wijn.[/]",
    "",
    "[#722F37]Ontdek bijzondere wijnen, leer meer over[/]",
    "[#722F37]druivenrassen en wijnregio's en leg je eigen[/]",
    "[#722F37]proefervaringen vast.[/]",
    "",
    "[italic #D4AF37]Elke fles vertelt een verhaal.[/]",
    "[italic #D4AF37]Jouw ontdekking begint hier![/]",
    "",
    Align.center(
        "[dim]Druk op Enter om naar het hoofdmenu te gaan...[/]"
        ),
    )

    console.print(default_panel(welcome_text))

def show_main_menu():
    """
    Displays the main menu.

    Input:
        None

    Output:
        Print main menu
    """
    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Wijnencyclopedie[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Wijnhuizen zoeken[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Wijn zoeken[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Mijn proefnotities[/]\n"
        "\n"
        "[dim]0. Afsluiten[/]"
    )

    console.print(default_panel(menu))

def show_encycl_menu():
    """
    Displays the encyclopedie menu.

    Input:
        None

    Output:
        Print encyclopedie menu
    """
    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Druiven[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Geuren[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Smaken[/]\n"
        "\n"
        "[dim]0. Afsluiten[/]"
    )

    console.print(default_panel(menu))

def menu_grapes():
    """
    Displays the grape color selection menu.

    Input:
        None

    Output:
        Returns the selected grape color.
    """

    global grapes_data

    if grapes_data is None:
        print("Druiven aan het plukken, kan even duren.")
        grapes_data = API_vinofyi.get_all_grapes()

    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Rood[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Wit[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Rosé[/]\n"
        "\n"
        "[dim]0. Terug[/]"
    )

    console.print(default_panel(menu))

    choice = menu_choice()

    colors = {
        1: "red",
        2: "white",
        3: "rose"
    }

    return colors.get(choice)

def menu_selection_grapes(grape_color):
    """
    Displays a list of grapes filtered by color.

    Input:
        grape_color = selected grape color

    Output:
        Displays matching grapes
    """

    global grapes_data

    grapes = [
        grape for grape in grapes_data
        if grape["color"] == grape_color
    ]

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Druif", style="#722F37")

    for number, grape in enumerate(grapes, start=1):
        table.add_row(f"{number}.", grape["name"])

    console.print(default_panel(table))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice > len(grapes):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_selection_grapes(grape_color)

    return grapes[choice - 1]

def show_grape_details(grape):
    """
    Displays information about a selected grape.

    Input:
        grape = selected grape dictionary

    Output:
        Displays grape information
    """

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Eigenschap", style="bold #D4AF37")
    table.add_column("Waarde", style="#722F37")

    table.add_row("Druif", grape.get("name", "-"))
    table.add_row("Kleur", grape.get("color", "-").capitalize())
    table.add_row("Land van oorsprong", grape.get("origin_country_name") or "-")
    table.add_row("Aantal wijnen", str(grape.get("wine_count", 0)))
    table.add_row("Beschrijving", grape.get("description") or "-")

    console.print(default_panel(table))

def menu_flavor():
    """
    Displays flavor categories and allows the user to select one.

    Input:
        None

    Output:
        Returns the selected flavor category.
    """

    global flavors_data

    if flavors_data is None:
        flavors_data = API_vinofyi.get_all_flavors()

    categories = sorted({
        flavor["category"]
        for flavor in flavors_data
    })

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Category", style="#722F37")

    for number, category in enumerate(categories, start=1):
        table.add_row(f"{number}.", category.capitalize())

    console.print(default_panel(table))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(categories):
        console.print("[red]Invalid choice.[/red]")
        return menu_flavor()

    return categories[choice - 1]

def menu_flavor_subcategories(category):
    """
    Displays subcategories belonging to the selected flavor category.

    Input:
        category = selected flavor category

    Output:
        Returns the selected subcategory.
    """

    global flavors_data

    subcategories = sorted({
        flavor["subcategory"]
        for flavor in flavors_data
        if flavor["category"] == category
    })

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Subcategory", style="#722F37")

    for number, subcategory in enumerate(subcategories, start=1):
        table.add_row(f"{number}.", subcategory.capitalize())

    content = Group(
        table,
        Align.center("[dim]0. Return to categories[/dim]")
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(subcategories):
        console.print("[red]Invalid choice.[/red]")
        return menu_flavor_subcategories(category)

    return subcategories[choice - 1]

def menu_flavor_results(category, subcategory):
    """
    Displays flavors belonging to the selected category and subcategory.

    Input:
        category = selected flavor category
        subcategory = selected flavor subcategory

    Output:
        Displays matching flavors
    """

    global flavors_data

    flavors = [
        flavor for flavor in flavors_data
        if flavor["category"] == category
        and flavor["subcategory"] == subcategory
    ]

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Flavor", style="#722F37")

    for number, flavor in enumerate(flavors, start=1):
        table.add_row(f"{number}.", flavor["name"])
    
    content = Group(
        table,
        Align.center("[dim]0. Return to main menu[/dim]")
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(flavors):
        console.print("[red]Invalid choice.[/red]")
        return menu_flavor_results(category, subcategory)

    return flavors[choice - 1]

def menu_aromas():
    """
    Displays aroma categories and allows the user to select one.

    Input:
        None

    Output:
        Returns the selected aroma category.
    """

    global flavors_data

    if flavors_data is None:
        flavors_data = API_vinofyi.get_all_flavors()

    categories = sorted({
        flavor["category"]
        for flavor in flavors_data
    })

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Categorie", style="#722F37")

    for number, category in enumerate(categories, start=1):
        table.add_row(f"{number}.", category.capitalize())

    content = Group(
        table,
        Align.center("[dim]0. Return to categories[/dim]")
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(categories):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_aromas()

    return categories[choice - 1]

def menu_aroma_results(category):
    """
    Displays aromas belonging to the selected category.

    Input:
        category = selected aroma category

    Output:
        Returns the selected aroma dictionary or None.
    """

    global flavors_data

    aromas = [
        flavor for flavor in flavors_data
        if flavor["category"] == category
    ]

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Aroma", style="#722F37")

    for number, aroma in enumerate(aromas, start=1):
        table.add_row(f"{number}.", aroma["name"])
    content = Group(
        table,
        Align.center("[dim]0. Return to main menu[/dim]")
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(aromas):
        console.print("[red]Invalid choice.[/red]")
        return menu_aroma_results(category)

    return aromas[choice - 1]

def menu_select_aromas():
    """
    Allows the user to select multiple aromas from different categories.

    Output:
        Returns a list of selected aromas.
    """

    selected_aromas = []

    while True:
        category = menu_aromas()

        if category is None:
            break

        aroma = menu_aroma_results(category)

        if aroma is not None:
            selected_aromas.append(aroma["name"])

        console.print(
            "[bold #D4AF37]Wil je nog een aroma toevoegen?[/]"
        )

        menu = (
            "[bold #D4AF37]1.[/] [#722F37]Ja[/]\n"
            "[bold #D4AF37]0.[/] [#722F37]Nee, verdergaan[/]"
        )

        console.print(default_panel(menu))

        if menu_choice() == 0:
            break

    return selected_aromas

def show_flavor_details(flavor):
    """
    Displays details of a selected aroma or flavor.

    Input:
        flavor = selected flavor dictionary

    Output:
        Returns to the previous menu.
    """

    content = Group(
        Align.center(
            f"[bold #D4AF37]{flavor['name']}[/]"
        ),
        Align.center(
            f"[dim]{flavor['category'].upper()} "
            f"· {flavor['subcategory'].upper()}[/]"
        ),
        flavor.get("description") or "No description available.",
        Align.center("[dim]Press Enter to go back[/dim]")
    )

    console.print(default_panel(content))
    input()

    return True

def menu_wineries():
    """
    Displays the winery search menu.

    Input:
        None

    Output:
        Print winery search menu
    """

    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Zoeken op naam[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Zoeken op land[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Random wijnhuis[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))
    return menu_choice()

def menu_search_winery():
    """
    Asks the user for a winery search term.

    Input:
        None

    Output:
        search_term = winery name entered by the user
    """

    console.print(default_panel(
        "[bold #D4AF37]Zoeken op naam[/]\n\n"
        "[#722F37]Voer de naam van een wijnhuis in.[/]"
    ))

    search_term = input("Zoekterm: ").strip()

    return search_term

def menu_winery_results(wineries):
    """
    Displays winery search results and lets the user select a winery.

    Input:
        wineries = list of found wineries

    Output:
        selected_winery = selected winery
    """

    table = Table(
        show_header=True,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Wijnhuis", style="#722F37")

    for number, winery in enumerate(wineries, start=1):
        table.add_row(f"{number}.", winery["name"])

    console.print(default_panel(table))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice > len(wineries):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_winery_results(wineries)

    return wineries[choice - 1]

def show_winery_details(winery):
    """Toont de details van een wijnhuis."""

    table = Table(
    show_header=False,
    box=None,
    padding=(0, 1),
    )

    table.add_column("Eigenschap", style="bold #D4AF37")
    table.add_column("Waarde", style="#722F37")

    table.add_row("Naam", winery.get("name", "-"))
    table.add_row("Land", winery.get("country", "-"))
    table.add_row("Regio", winery.get("region", "-"))
    table.add_row("Website", winery.get("website", "-"))
    table.add_row("Aantal wijnen", str(winery.get("wine_count", 0)))

    description = winery.get("description")

    if description:
        description_panel = Panel(
            description,
            title="[bold #D4AF37]Over het wijnhuis[/bold #D4AF37]",
            border_style="#722F37",
            padding=(1, 2),
        )
    else:
        description_panel = None

    wines = winery.get("top_wines", [])

    if wines:
        wine_table = Table(
            title="[bold #D4AF37]Wijnen van dit wijnhuis[/bold #D4AF37]",
            show_header=True,
            box=None,
            padding=(0, 1),
        )

        wine_table.add_column("Nr.", style="bold #D4AF37", justify="right")
        wine_table.add_column("Wijn", style="#722F37")
        wine_table.add_column("Type", style="#722F37")
        wine_table.add_column("Beoordeling", style="#D4AF37", justify="right")

        for number, wine in enumerate(wines, start=1):
            wine_table.add_row(
                f"{number}.",
                wine.get("name", "-"),
                wine.get("wine_type", "-"),
                str(wine.get("avg_rating") or "-")
            )

    content_items = [table]

    if description:
        content_items.append(description_panel)

    if wines:
        content_items.append(wine_table)

    content_items.append(
        Align.center("[dim]Kies voor 0 om terug te keren naar het Hoofdmenu[/dim]")
    )

    content = Group(*content_items)

    console.print(default_panel(content))
    choice = menu_choice()

    if choice is None:
        return None

    if choice > len(wines):
        console.print("[red]Ongeldige keuze.[/red]")
        return None

    return wines[choice - 1]

def menu_countries():
    """Menu om voorgeselecteerde landen te laten zien."""
    countries = {
        1: "netherlands",
        2: "germany",
        3: "france",
        4: "italy"
    }

    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Nederland[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Duitsland[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Frankrijk[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Italië[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))
    choice = menu_choice()

    if choice == 0:
        return None

    if choice not in countries:
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_countries()

    return countries[choice]

def menu_regions(regions):
    """Toont regio's en laat de gebruiker er één selecteren."""

    table = Table(
        show_header=True,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Regio", style="#722F37")
    table.add_column("Wijnhuizen", justify="right")

    for number, region in enumerate(regions, start=1):
        table.add_row(
            f"{number}.",
            region["name"],
            str(region["winery_count"])
        )

    console.print(default_panel(table))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice > len(regions):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_regions(regions)

    return regions[choice - 1]

def menu_wine_results(wines):
    """
    Displays wine search results and lets the user select a wine.

    Input:
        wines = list of found wines

    Output:
        selected_wine = selected wine or None
    """

    table = Table(
        show_header=True,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Wijn", style="#722F37")
    table.add_column("Wijnhuis", style="#722F37")
    table.add_column("Regio", style="#722F37")
    table.add_column("Land", style="#722F37")
    table.add_column("Jaargang", style="#722F37")

    for number, wine in enumerate(wines, start=1):
        table.add_row(
            f"{number}.",
            wine.get("name", "-"),
            wine.get("winery", "-"),
            wine.get("region", "-"),
            wine.get("country", "-"),
            str(wine.get("vintage") or "-")
        )

    console.print(default_panel(table))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice > len(wines):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_wine_results(wines)

    return wines[choice - 1]

def menu_search_wine():
    """
    Asks the user to enter a wine search term.

    Output:
        search_term = entered search term
    """
    return console.input("[bold]Zoek een wijn: [/bold]").strip()

def show_wine_details(wine):
    """
    Displays information about a selected wine.

    Input:
        wine = selected wine object

    Output:
        Displays wine information
    """

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Eigenschap", style="bold #D4AF37")
    table.add_column("Waarde", style="#722F37")

    table.add_row("Wijn", wine.get("name", "-"))
    table.add_row(
        "Wijnhuis",
        wine.get("winery", {}).get("name", "-")
    )
    table.add_row("Type", wine.get("wine_type", "-"))
    table.add_row("Regio", wine.get("region", "-"))
    table.add_row("Land", wine.get("country", "-"))
    table.add_row("Jaargang", str(wine.get("vintage") or "-"))
    table.add_row("Gemiddelde beoordeling", str(wine.get("avg_rating", "-")))
    table.add_row("Aantal beoordelingen", str(wine.get("rating_count", "-")))

    grapes = wine.get("grapes") or []

    grape_names = []

    for grape in grapes:
        name = grape.get("name", "-")
        percentage = grape.get("percentage")

        if percentage is not None:
            name += f" ({percentage}%)"

        grape_names.append(name)

    table.add_row(
        "Druivensoorten",
        ", ".join(grape_names) if grape_names else "-"
    )

    content = Group(
        table,
        Align.center("[dim]Druk op Enter om verder te gaan[/dim]")
    )

    console.print(default_panel(content))
    input()

def menu_tasting_notes(tasting_notes):
    """
    Displays saved tasting notes and allows the user to select one.

    Input:
        tasting_notes = list of saved tasting notes

    Output:
        Returns the selected tasting note or None.
    """

    table = Table(
        show_header=True,
        box=None,
        padding=(0, 1)
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Wijn", style="#722F37")
    table.add_column("Wijnhuis", style="#722F37")
    table.add_column("Datum", style="#722F37")
    table.add_column("Beoordeling", style="#D4AF37")

    for number, note in enumerate(tasting_notes, start=1):
        table.add_row(
            f"{number}.",
            note["wine"]["name"] or "-",
            note["wine"]["winery"] or "-",
            note["date"],
            note["conclusion"]["liked"]
        )

    content = Group(
        table,
        Align.center("[dim]0. Terug naar hoofdmenu[/dim]")
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(tasting_notes):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_tasting_notes(tasting_notes)

    return tasting_notes[choice - 1]

def show_tasting_note_details(tasting_note):
    """
    Displays the complete details of a tasting note.

    Input:
        tasting_note = selected tasting note dictionary

    Output:
        Displays the tasting note.
    """

    wine = tasting_note["wine"]
    appearance = tasting_note["appearance"]
    aroma = tasting_note["aroma"]
    taste = tasting_note["taste"]
    conclusion = tasting_note["conclusion"]

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1)
    )

    table.add_column("Eigenschap", style="bold #D4AF37")
    table.add_column("Waarde", style="#722F37")

    table.add_row("Wijn", wine.get("name") or "-")
    table.add_row("Wijnhuis", wine.get("winery") or "-")
    table.add_row("Jaargang", str(wine.get("vintage") or "-"))
    table.add_row("Datum", tasting_note.get("date", "-"))

    table.add_row("Kleur", appearance.get("color", "-"))
    table.add_row("Helderheid", appearance.get("clarity", "-"))

    table.add_row("Geurintensiteit", aroma.get("intensity", "-"))
    table.add_row(
        "Aroma's",
        ", ".join(aroma.get("aromas", [])) or "-"
    )

    table.add_row("Zuren", taste.get("acidity", "-"))
    table.add_row("Zoetheid", taste.get("sweetness", "-"))
    table.add_row("Body", taste.get("body", "-"))
    table.add_row("Tannines", taste.get("tannins", "-"))
    table.add_row("Geur en smaak", taste.get("aroma_match", "-"))

    table.add_row("Afdronk", conclusion.get("finish", "-"))
    table.add_row("Balans", conclusion.get("balance", "-"))
    table.add_row("Wijn lekker?", conclusion.get("liked", "-"))
    table.add_row("Toelichting", conclusion.get("reason", "-"))

    content = Group(
        table,
        Align.center("[dim]Druk op Enter om terug te gaan[/dim]")
    )

    console.print(default_panel(content))
    input()

def menu_tasting_notes_main():
    """
    Displays the tasting notes menu.

    Output:
        Returns the selected menu option.
    """

    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Nieuwe proefnotitie maken[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Proefnotities bekijken[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Proefnotitie aanpassen[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Proefnotitie verwijderen[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))

    return menu_choice()

def menu_choice():
    """
    returns menu choice in integer.

    Input:
        None

    Output:
        choice = integer menu choice
    """
    while True:
        choice = input('Maak een keuze: ')

        if not choice.isdigit():
            print('Geen geldige keuze, voer een getal in.')
            continue

        return int(choice)

def menu_select_option(question, options):
    """
    Displays a question with selectable answer options.

    Input:
        question = question to display
        options = list of possible answers

    Output:
        Returns the selected answer or None.
    """

    menu = "\n".join(
        f"[bold #D4AF37]{number}.[/] [#722F37]{option}[/]"
        for number, option in enumerate(options, start=1)
    )

    content = Group(
        f"[bold #D4AF37]{question}[/]\n",
        menu,
        "\n[dim]0. Terug[/]"
    )

    console.print(default_panel(content))

    choice = menu_choice()

    if choice == 0:
        return None

    if choice < 1 or choice > len(options):
        console.print("[red]Ongeldige keuze.[/red]")
        return menu_select_option(question, options)

    return options[choice - 1]