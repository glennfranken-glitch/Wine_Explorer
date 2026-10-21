from rich.console import Console
from rich.panel import Panel

console = Console()

def default_panel(text):
    panel = Panel(
    text,
    title= "[bold #722F37]🍷 Wine Explorer[/]",
    border_style="bold #D4AF37",
    style="#F4EBDD",
    padding=(1, 4)
              )

    return panel