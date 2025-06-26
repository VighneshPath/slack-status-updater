import pytest
from slack_status_updater.slack_client import SlackStatusUpdater

def test_update_status_success(requests_mock):
    token = "fake-token"
    requests_mock.post(
        "https://slack.com/api/users.profile.set",
        json={"ok": True},
        status_code=200
    )

    updater = SlackStatusUpdater(token)
    updater.update_status("In a test", ":test_tube:")

def test_update_status_failure(requests_mock):
    token = "fake-token"
    requests_mock.post(
        "https://slack.com/api/users.profile.set",
        json={"ok": False, "error": "invalid_auth"},
        status_code=200
    )

    updater = SlackStatusUpdater(token)
    with pytest.raises(RuntimeError, match="Slack API error"):
        updater.update_status("Failing test", ":x:")