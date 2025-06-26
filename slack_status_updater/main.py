from .cli import set_status

import typer

app = typer.Typer()
app.command()(set_status)