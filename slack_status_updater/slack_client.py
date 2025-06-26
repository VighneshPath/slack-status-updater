import requests
from .interfaces import StatusUpdater

class SlackStatusUpdater(StatusUpdater):
    def __init__(self, token: str):
        self.token = token
        self.api_url = "https://slack.com/api/users.profile.set"

    def update_status(self, text: str, emoji: str, expiration: int = 0) -> None:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        profile = {
            "status_text": text,
            "status_emoji": emoji,
            "status_expiration": expiration
        }
        response = requests.post(self.api_url, json={"profile": profile}, headers=headers)
        if not response.ok or not response.json().get("ok", False):
            raise RuntimeError(f"Slack API error: {response.text}")