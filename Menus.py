from ast import Global

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
        "[bold #D4AF37]3.[/] [#722F37]Mijn proefnotities[/]\n"
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

def menu_countries():
    #
    menu = (
        "[bold #D4AF37]1.[/] [#722F37]Nederland[/]\n"
        "[bold #D4AF37]2.[/] [#722F37]Duitsland[/]\n"
        "[bold #D4AF37]3.[/] [#722F37]Frankrijk[/]\n"
        "[bold #D4AF37]4.[/] [#722F37]Italië[/]\n"
        "\n"
        "[dim]0. Terug naar hoofdmenu[/]"
    )

    console.print(default_panel(menu))

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