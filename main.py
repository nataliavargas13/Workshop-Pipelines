#imports
import requests
import pandas as pd
import re
import json
import math

import os       #acquisition methods ver lesson
from dotenv import load_dotenv


load_dotenv('../.env')
TOKEN = os.environ.get("API_TOKEN")

API_TOKEN = TOKEN
USERNAME = 'nataliavargas13/'
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = 'dataptmad0923_labs/'
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'
BASE_URL + KEY + OWNER + REPO + PULLS


def pages(BASE_URL, SEARCH, STATE , USERNAME, TOKEN):
    pages = requests.get(BASE_URL + search.format(STATE), auth=(USERNAME,TOKEN)).json()['total_count']
    if STATE == 'open':
        pages = math.ceil(pages/100)
        return pages
    elif STATE == 'closed':
        pages = math.ceil(pages/100)
        return pages