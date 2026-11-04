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

def menu_flavor():
    #check if flavor data is filled if yes do not make API request
    global flavors_data
    if flavors_data is None:
        flavors_data = API_vinofyi.get_all_flavors()

    categories = set()

    for flavor in flavors_data:
        categories.add(flavor["category"])

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Categorie", style="#722F37")

    for number, category in enumerate(sorted(categories), start=1):
        table.add_row(f"{number}.", category.capitalize())

    console.print(default_panel(table))

    return categories

def menu_grapes():
    #check if grapes data is filled if yes do not make API request
    global grapes_data
    if grapes_data is None:
        print("Druiven aan het plukken, kan even duren.")
        grapes_data = API_vinofyi.get_all_grapes()

    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Rood[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Wit[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Rosé[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Nouserend[/]\n"
        "\n"
        "[dim]0. Terug[/]"
    )
    
    console.print(default_panel(menu))

def menu_selection_grapes(type):
    global grapes_data

    menu = (
        f"[bold #D4AF37]1.[/] [#722F37]Lijst met {type} druiven[/]\n"
        f"[bold #D4AF37]2.[/] [#722F37]Lijst met {type} druiven[/]\n"
        f"[bold #D4AF37]3.[/] [#722F37]Lijst met {type} druiven[/]\n"
        f"[bold #D4AF37]4.[/] [#722F37]Lijst met {type} druiven[/]\n"
        "\n"
        "[dim]0. Terug[/]"
    )
    
    console.print(default_panel(menu))

def menu_aromas():
    """
    Toont de beschikbare geurcategorieën en laat de gebruiker een keuze maken.

    :return: De gekozen geurcategorie.
    :rtype: str
    """
    global flavors_data

    #Haal de gegevens alleen op als flavors_data nog leeg is
    if not flavors_data:
        flavors_data = API_vinofyi.get_all_flavors()

    categories = set()

    for flavor in flavors_data:
        categories.add(flavor["category"])

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Nr.", style="bold #D4AF37", justify="right")
    table.add_column("Categorie", style="#722F37")

    for number, category in enumerate(sorted(categories), start=1):
        table.add_row(f"{number}.", category.capitalize())

    console.print(default_panel(table))

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
        "[bold #D4AF37]3.[/] [#722F37]Zoeken op appellatie[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Random wijnhuis[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))

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
        show_header=False,
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
        Align.center("[dim]Druk op Enter om verder te gaan[/dim]")
    )

    content = Group(*content_items)

    console.print(default_panel(content))
    input()

def menu_countries():
    """Menu om voorgeselecteerde landen te laten zien"""
    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Nederland[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Duitsland[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Frankrijk[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Italië[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))

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
    table.add_row("Wijnhuis", wine.get("winery", "-"))
    table.add_row("Type", wine.get("type", "-"))
    table.add_row("Regio", wine.get("region", "-"))
    table.add_row("Land", wine.get("country", "-"))
    table.add_row("Jaargang", str(wine.get("vintage") or "-"))
    table.add_row("Gemiddelde beoordeling", str(wine.get("averageRating", "-")))
    table.add_row("Aantal beoordelingen", str(wine.get("ratingsCount", "-")))

    content = Group(
        table,
        Align.center("[dim]Druk op Enter om verder te gaan[/dim]")
    )

    console.print(default_panel(content))
    input()

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