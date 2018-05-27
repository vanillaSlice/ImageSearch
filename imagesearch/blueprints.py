"""
Exports ImageSearch app blueprints.
"""

from flask import Blueprint, jsonify, render_template, request

from .helpers import (get_app_url, 
                      get_latest_searches,
                      save_search_to_database,
                      search_images)

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/")
def index():
    return render_template("home.html", app_url=get_app_url())

@home.route("/search/<terms>")
def search(terms):
    offset = request.args.get("offset", 1, type=int)
    images = search_images(terms, offset)
    save_search_to_database(terms)
    return jsonify(images)

@home.route("/latest")
def latest():
    return jsonify(get_latest_searches())
