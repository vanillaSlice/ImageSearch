"""
Exports ImageSearch app blueprints.
"""

from flask import Blueprint, jsonify, redirect, request

from .helpers import (get_latest_searches,
                      save_search_to_database,
                      search_images)

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/")
def index():
    """
    Index route.
    """

    return redirect('/ui')

@home.route("/search/<terms>")
def search(terms):
    """
    Search route.
    """

    offset = request.args.get("offset", 1, type=int)
    images = search_images(terms, offset)
    save_search_to_database(terms)
    return jsonify(images)

@home.route("/latest")
def latest():
    """
    Latest route.
    """

    return jsonify(get_latest_searches())
