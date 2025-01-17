from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def exibir_menu():
    texto_menu = Text("MENU", style="bold magenta")
    texto_menu.append("\n")
    texto_menu.append("1. Opção 1\n")
    texto_menu.append("2. Opção 2\n")
    texto_menu.append("3. Opção 3\n")
    texto_menu.append("0. Sair")

    panel = Panel(texto_menu, title="Escolha uma opção", border_style="green")
    console.print(panel)

while True:
    exibir_menu()
    opcao = console.input("[bold blue]Opção: [/bold blue]")
    # ... (mesma lógica de antes para lidar com as opções)
