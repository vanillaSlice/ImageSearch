"""
Helper functions.
"""

from flask import current_app as app, request
import requests

from .models import SearchEntry

def search_images(terms, offset):
    """
    Returns search results.
    """

    payload = {"key": app.config["GOOGLE_API_KEY"],
               "cx": app.config["GOOGLE_CSE_ID"],
               "q": terms,
               "start": offset,
               "searchType": "image"}
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=payload)

    images = []
    for item in response.json()["items"]:
        images.append({
            "url": item["link"],
            "snippet": item["snippet"],
            "thumbnail": item["image"]["thumbnailLink"],
            "context": item["image"]["contextLink"]
        })

    return images

def save_search_to_database(terms):
    """
    Saves search to database.
    """

    SearchEntry(terms).save()

def get_latest_searches():
    """
    Returns latest searchs.
    """

    latest_searches = SearchEntry.objects.order_by("-when").limit(10)
    latest_searches_as_json = []
    for search in latest_searches:
        latest_searches_as_json.append(search.to_json())
    return latest_searches_as_json

def get_app_url():
    """
    Returns app url.
    """

    if app.config.get("SSL"):
        return request.host_url.replace("http://", "https://")
    else:
        return request.host_url
