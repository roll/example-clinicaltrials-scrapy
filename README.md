# Scraper Boilerplate for clinicaltrials.gov

A clinicaltrials.gov scraper boilerplate based on the Scrapy framework.

## Prerequisite

- sudo apt-get install libffi-dev
- sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev

## Quick Start

```bash
virtualenv venv -p python2
source venv/bin/activate
pip install -r requirements.txt
scrapy crawl trials
```

Scraped data will be in the data directory.
