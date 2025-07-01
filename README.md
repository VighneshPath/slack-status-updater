## 🚀 Installation

You can install the CLI tool directly from GitHub using [`uv`](https://github.com/astral-sh/uv):

```bash
uv pip install git+https://github.com/VighneshPath/slack-status-updater --system
```

> ℹ️ Make sure you have Python 3.8+ and `uv` installed:
>
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

---

## 🛠️ Configuration

Generating a token

Go to https://api.slack.com/apps and follow the instructions mentioned below

https://github.com/user-attachments/assets/f27689b0-f84b-4090-9033-0e7ccea8fe8a

Create a `.env` file in your home directory under `~/.slack-status` or project root with your Slack API token:

```
SLACK_API_TOKEN=xoxp-your-token-here
```

For conveninence
```
mkdir -p ~/.slack-status && echo "SLACK_API_TOKEN=xoxp-your-token-here" > ~/.slack-status/.env
```

Or you can pass the token directly as a CLI option.

---

## ✅ Usage

### Set Slack Status

```bash
slack-status set-status --text "Working from home" --emoji ":house:" --duration 1d
```

| Option         | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| `--text`       | Status message text (required)                                 |
| `--emoji`      | Emoji code (e.g. `:house:`) (required)                         |
| `--duration`   | How long to keep status (e.g. 1d, 2h, 30m, 0 = no expiration)  |
| `--token`      | (Optional) Pass token directly if not using `.env`             |

---

### Remove Slack Status

```bash
slack-status remove-status
```

| Option         | Description                                        |
| -------------- | -------------------------------------------------- |
| `--token`      | (Optional) Pass token directly if not using `.env` |

---

### Useful shell functions along with their usage

Add these to your `~/.bashrc or ~/.zshrc` for using these functions

```
sstt() {
  slack-status set-status --text "TT" --emoji ":table_tennis_paddle_and_ball:" --duration "${1:-45m}"
}

ssrm() {
  slack-status remove-status
}

sswfh() {
  slack-status set-status --text "WFH" --emoji ":house:" --duration "${1:-1d}"
}

ssl() {
  slack-status set-status --text "Lunch" --emoji ":knife_fork_plate:" --duration "${1:-30m}"
}

ssc() {
  slack-status set-status --text "Brewing Coffee" --emoji ":coffee:" --duration "${1:-15m}"
}
```

Usage - 

```
sstt
```
This will update your slack status with the text TT and emoji :table_tennis_paddle_and_ball: for a default of 45m

```
sstt 30m
```
This will update your slack status with the text TT and emoji :table_tennis_paddle_and_ball: for 30m


## 🧪 Local Testing

To run tests:

```bash
uv pip install .[dev]
pytest
```
