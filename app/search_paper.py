from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

current_year = datetime.now().year
limitSearch = 100000
limitView = 100000


# Fungsi untuk mencari dokumen berdasarkan query
def search_papers(
    collection, query, sort="relevance", yearFilter="all", limit=limitView
):
    documents = list(
        collection.find(
            {},
            {
                "title": 1,
                "abstract": 1,
                "_id": 1,
                "year": 1,
                "n_citation": 1,
                "venue": 1,
                "authors": 1,
            },
        ).limit(limitSearch)
    )
    combined_documents = [
        f"{doc.get('title', '')} {doc.get('abstract', '')}" for doc in documents
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_documents + [query])
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    for i, doc in enumerate(documents):
        doc["score"] = similarity_scores[i]

    ranked_documents = sorted(documents, key=lambda x: x["score"], reverse=True)

    data = []
    for doc in ranked_documents[:limit]:
        if doc["score"] == 0:
            continue

        authors = doc.get("authors", [])
        if isinstance(authors, str):
            try:
                authors = eval(authors)
            except Exception:
                authors = [authors]

        data.append(
            {
                "score": doc["score"],
                "title": doc.get("title", "Unknown"),
                "abstract": doc.get("abstract", "Unknown"),
                "venue": doc.get("venue", "Unknown"),
                "year": str(doc.get("year", "Unknown")),
                "n_citation": doc.get("n_citation", 0),
                "authors": authors,
                "id": str(doc["_id"]),
            }
        )

    if yearFilter != "all":
        year_range = int(yearFilter)
        start_year = current_year - year_range
        data = [x for x in data if int(x["year"]) >= start_year]

    if sort == "relevance":
        data = sorted(data, key=lambda x: x["score"], reverse=True)
    elif sort == "year":
        data = sorted(data, key=lambda x: x["year"], reverse=True)
    elif sort == "citations":
        data = sorted(data, key=lambda x: x["n_citation"], reverse=True)
    elif sort == "title":
        data = sorted(data, key=lambda x: x["title"].lower())

    return data
