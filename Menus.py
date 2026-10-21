from rich.console import Console
from rich.panel import Panel

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
    main_menu = default_panel(menu)
    console.print(main_menu)