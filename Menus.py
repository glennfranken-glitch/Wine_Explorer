from rich.console import Console
from rich.panel import Panel
from rich.console import Group
from rich.align import Align

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