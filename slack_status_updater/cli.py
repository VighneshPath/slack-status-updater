import datetime
import typer
from .config import get_slack_token
from .slack_client import SlackStatusUpdater


def parse_duration(duration: str) -> int:
    """
    Parses a duration string (e.g., "2h", "45m") into seconds.
    """
    if duration.endswith("d"):
        return int(duration[:-1]) * 86400
    elif duration.endswith("h"):
        return int(duration[:-1]) * 3600
    elif duration.endswith("m"):
        return int(duration[:-1]) * 60
    elif duration.endswith("s"):
        return int(duration[:-1])
    elif duration == "0":
        return 0
    else:
        raise typer.BadParameter("Duration must be like 1d, 2h, 30m, 45s or 0")


def set_status(
    text: str = typer.Option(..., help="Slack status text"),
    emoji: str = typer.Option(..., help="Slack status emoji"),
    duration: str = typer.Option("0", help="How long to keep status (e.g. 1d, 2h, 30m, 0 = no expiration)"),
    token: str = typer.Option(None, help="Slack API token (overrides env)")
):
    """Set your Slack status."""
    try:
        expiration_seconds = parse_duration(duration)
        expiration_ts = int((datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(seconds=expiration_seconds)).timestamp()) if expiration_seconds else 0

        slack_token = token or get_slack_token()
        updater = SlackStatusUpdater(slack_token)
        updater.update_status(text, emoji, expiration=expiration_ts)

        msg = f"✅ Status updated (expires in {duration})" if expiration_ts else "✅ Status updated (no expiration)"
        typer.echo(msg)

    except Exception as e:
        typer.secho(f"❌ {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
