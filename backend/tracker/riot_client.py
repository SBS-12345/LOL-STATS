import os
import time

import requests
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://americas.api.riotgames.com"
header = {"X-Riot-Token": os.getenv("RIOT_API_KEY")}

# Helper function for calling different APIs

def _get(endpoint, params=None):
    if params is None:
        params = {}

    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params, headers=header)
    response.raise_for_status()

    time.sleep(1.2) # For dealing with the Riot API Rate Limiting

    return response.json()

# Getting the account information
def get_account(game_name, tag_line):
    endpoint = f"/riot/account/v1/accounts/by-riot-id/{quote(game_name)}/{quote(tag_line)}"
    return _get(endpoint)

# Getting the match IDs
def get_match_ids(puuid, num_matches = 20, match_type = "ranked"):
    query_parameters = {
        "type" : match_type,
        "count" : num_matches
    }
    endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    return _get(endpoint, query_parameters)

# Getting the match description from the match ID
def get_matches(match_id):
    endpoint = f"/lol/match/v5/matches/{match_id}"
    return _get(endpoint)