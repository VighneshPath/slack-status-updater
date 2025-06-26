## 🚀 Installation

You can install the CLI tool directly from GitHub using [`uv`](https://github.com/astral-sh/uv):

```bash
uv pip install git+https://github.com/VighneshPath/slack-status-updater
```

> ℹ️ Make sure you have Python 3.8+ and `uv` installed:
>
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

---

## 🛠️ Configuration

Create a `.env` file in your home directory or project root with your Slack API token:

```
SLACK_API_TOKEN=xoxp-your-token-here
```

Or you can pass the token directly as a CLI option.

---

## ✅ Usage

### Set Slack Status

```bash
slack-status --text "Working remotely" --emoji ":house:" --expiration 3600
```

| Option         | Description                                        |
| -------------- | -------------------------------------------------- |
| `--text`       | Status message text (required)                     |
| `--emoji`      | Emoji code (e.g. `:house:`) (required)             |
| `--expiration` | Optional duration in seconds (e.g. 3600 = 1 hour)  |
| `--token`      | (Optional) Pass token directly if not using `.env` |

---

## 🧪 Local Testing

To run tests:

```bash
uv pip install .[dev]
pytest
```
