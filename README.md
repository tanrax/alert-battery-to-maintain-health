<p align="center">
    <img src="icons/battery-status.png" width="200"> 
</p>

Alerts you if your battery is overcharged 🌹 or discharged 🥀 to extend its performance and health.

**Only Linux**: Want more compatible systems? I look forward to your pull requests to add more notification systems. Check line 25 in `src/__main__.py`.

# Preview

<p align="center">
    <img src="media/demo.png" width="500"> 
</p>

# Install

```bash
git clone git@github.com:tanrax/alert-battery-to-maintain-health.git
cd alert-battery-to-maintain-health
poetry install
```

# Run

```bash
poetry run python3 src
```

# Cron

```bash
crontab -e
```

Add the following:

```bash
* * * * * 'cd [absolute path folder] && poetry run python3 src'
```
