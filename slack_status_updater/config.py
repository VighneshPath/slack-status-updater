import os
from pathlib import Path
from dotenv import load_dotenv

def load_env_from_default_locations():
    possible_paths = [
        Path.cwd() / ".env",
        Path.home() / ".slack-status" / ".env",
        Path.home() / ".config" / "slack-status" / ".env",
    ]

    for path in possible_paths:
        if path.exists():
            load_dotenv(dotenv_path=path)
            return

    load_dotenv()

load_env_from_default_locations()
def get_slack_token() -> str:
    token = os.getenv("SLACK_API_TOKEN")
    if not token:
        raise EnvironmentError("Missing SLACK_API_TOKEN in environment or .env file")
    return token