# Web Scraper Project

## Overview

A web scraper built with Flask and SQLAlchemy for scraping and storing web data.

## Features

- User authentication
- Data scraping
- Data storage

## Requirements

- Python 3.8+
- See `requirements.txt` for full list

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Anastasios3/webScrapper.git
   cd webScrapper


Create a virtual environment:

sh

python -m venv scraper_env
scraper_env\Scripts\activate  # On Windows
source scraper_env/bin/activate  # On Unix/macOS

Install dependencies:

sh

pip install -r requirements.txt

Set up the database:

sh

    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()

Usage

    Run the app:

    sh

    python run.py

    Open in browser:
    Navigate to http://127.0.0.1:5000/.

License

MIT License
