import os

# Platform

PLATFORM = os.getenv('PLATFORM')
if not PLATFORM:
    PLATFORM = 'DEVELOPMENT'

# General

BOT_NAME = 'clinicaltrials'
SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# Throttle

DOWNLOAD_DELAY = 3
AUTOTHROTTLE_ENABLED = True

# Pipelines

ITEM_PIPELINES = {
    'pipelines.Normalize': 200,
    'pipelines.Jsonfile': 250,
}

# Database

# DATABASE_HOST = os.environ['XXX_HOST']
# DATABASE_PORT = os.environ['XXX_PORT']
# DATABASE_USER = os.environ['XXX_USER']
# DATABASE_PASS = os.environ['XXX_PASS']
# DATABASE_INDEX = 'development'

# if PLATFORM == 'STAGING':
    # DATABASE_INDEX = 'staging'

# if PLATFORM == 'PRODUCTION':
    # DATABASE_INDEX = 'production'
