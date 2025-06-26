import typer
from .config import get_slack_token
from .slack_client import SlackStatusUpdater

def set_status(
    text: str = typer.Option(..., help="Slack status text"),
    emoji: str = typer.Option(..., help="Slack status emoji"),
    expiration: int = typer.Option(0, help="Expiration time in seconds"),
    token: str = typer.Option(None, help="Slack API token (overrides env)")
):
    """Set your Slack status."""
    try:
        slack_token = token or get_slack_token()
        updater = SlackStatusUpdater(slack_token)
        updater.update_status(text, emoji, expiration)
        typer.echo("✅ Status updated successfully.")
    except Exception as e:
        typer.secho(f"❌ {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)