from typing import Any, Dict, List, Union
from dotenv import load_dotenv
import os

# obtain API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# type aliases
JSONType = Union[Dict[str, Any], List[Any]]


# API configuraiton
API_URL = "https://trashnothing.com/api/v1.4/posts"
API_HEADERS = {

}
API_PARAMS = {
    "api_key": api_key,
    "sort_by": "date",
    "types": "offer",
    "sources": "groups",
    "group_ids": 4673, # DC ReUseIt group
    "per_page": 5,
    "page": 1,
}


# Output file configuration
CSV_OUTPUT_PATH = "/Users/morgan/Documents/16_ArjanCodes/next_level_python/whiskey_auction/data/trash_posts.csv"
