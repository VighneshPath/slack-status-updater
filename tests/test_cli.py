import os
import pytest
from typer.testing import CliRunner
from slack_status_updater.main import app

runner = CliRunner()

def test_cli_success(monkeypatch, requests_mock):
    requests_mock.post(
        "https://slack.com/api/users.profile.set",
        json={"ok": True},
        status_code=200
    )
    monkeypatch.setenv("SLACK_API_TOKEN", "fake-token")

    result = runner.invoke(app, ["--text", "Testing", "--emoji", ":bug:"])
    assert result.exit_code == 0
    assert "✅" in result.stdout

def test_cli_missing_token(monkeypatch):
    monkeypatch.delenv("SLACK_API_TOKEN", raising=False)

    result = runner.invoke(app, ["--text", "Missing token", "--emoji", ":lock:"])
    assert result.exit_code != 0
    assert "Missing SLACK_API_TOKEN" in result.stdout
