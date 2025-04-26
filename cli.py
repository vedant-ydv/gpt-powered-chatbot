"""Command-line interface for the AI chatbot."""
import typer
from rich.console import Console
from rich.markdown import Markdown
from .chat import ChatBot

app = typer.Typer()
console = Console()
chatbot = ChatBot()

@app.command()
def main():
    """Start an interactive chat session with the AI."""
    console.print("[bold green]Welcome to AI ChatBot![/bold green]")
    console.print("Type 'quit' to exit, 'clear' to clear history\n")
    
    while True:
        user_input = console.input("[bold blue]You:[/bold blue] ")
        
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'clear':
            chatbot.clear_history()
            console.print("[yellow]Chat history cleared[/yellow]")
            continue
        
        try:
            response = chatbot.chat(user_input)
            console.print("\n[bold green]AI:[/bold green]")
            console.print(Markdown(response))
            console.print()
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    app() 