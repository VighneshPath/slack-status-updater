from typer.testing import CliRunner
from slack_status_updater.main import app
from slack_status_updater.cli import parse_duration

runner = CliRunner()

def test_cli_success(monkeypatch, requests_mock):
    requests_mock.post(
        "https://slack.com/api/users.profile.set",
        json={"ok": True},
        status_code=200
    )
    monkeypatch.setenv("SLACK_API_TOKEN", "fake-token")

    result = runner.invoke(app, ["set-status", "--text", "Testing", "--emoji", ":bug:"])
    assert result.exit_code == 0
    assert "✅" in result.stdout

def test_cli_missing_token(monkeypatch):
    monkeypatch.delenv("SLACK_API_TOKEN", raising=False)

    result = runner.invoke(app, ["set-status", "--text", "Missing token", "--emoji", ":lock:"])
    assert result.exit_code != 0
    assert "Missing SLACK_API_TOKEN" in result.stdout


def test_cli_remove_status_success(monkeypatch, requests_mock):
    requests_mock.post(
        "https://slack.com/api/users.profile.set",
        json={"ok": True},
        status_code=200
    )
    monkeypatch.setenv("SLACK_API_TOKEN", "fake-token")

    result = runner.invoke(app, ["remove-status"])
    assert result.exit_code == 0
    assert "✅" in result.stdout

def test_cli_remove_status_missing_token(monkeypatch):
    monkeypatch.delenv("SLACK_API_TOKEN", raising=False)

    result = runner.invoke(app, ["remove-status"])
    assert result.exit_code != 0
    assert "Missing SLACK_API_TOKEN" in result.stdout


def test_parse_duration():
    assert parse_duration("2h") == 7200
    assert parse_duration("30m") == 1800
    assert parse_duration("45s") == 45
    assert parse_duration("0") == 0
