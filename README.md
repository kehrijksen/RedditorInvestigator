# RedditorInvestigator
Scrape users of reddit.com using praw

## Installation
**Setup virtual environments:**

`python -m venv .`

**Activate virtual environments:**

Windows:
`.\venv\Scripts\activate.bat`

Linux:
`.\venv\Scripts\activate`

**Install modules:**

`pip install -r requirements.txt`

## API setup
Windows:
`copy example.env .env`

Linux:
`cp example.env .env`

Go to https://www.reddit.com/prefs/apps

Fill in a random name and http://127.0.0.1:1337

Paste the variables into .env
