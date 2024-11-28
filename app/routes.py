from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from .search_paper import search_papers

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["research_paper_dataset"]
collection = db["research_paper"]

# Blueprint untuk routing
bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    sort = request.args.get("sort", "relevance")
    yearFilter = request.args.get("yearFilter", "")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = search_papers(collection, query, sort=sort, yearFilter=yearFilter)
    return jsonify(results)
