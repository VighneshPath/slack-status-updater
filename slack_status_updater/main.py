from .cli import remove_status, set_status

import typer

app = typer.Typer()
app.command()(set_status)
app.command(name="remove-status")(remove_status)