from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request, jsonify

# Setup Flask app
app = Flask(__name__)

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['research_paper_dataset']
collection = db['research_paper']

# Fungsi untuk mencari dokumen berdasarkan query
def search_papers(query, sort="relevance", limit=10):
    documents = list(collection.find({}, {"title": 1, "abstract": 1, "_id": 1, "year": 1, "citations": 1}).limit(100000))
    combined_documents = [f"{doc.get('title', '')} {doc.get('abstract', '')}" for doc in documents]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_documents + [query])
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    for i, doc in enumerate(documents):
        doc["score"] = similarity_scores[i]

    if sort == "year":
        ranked_documents = sorted(documents, key=lambda x: x.get("year", 0), reverse=True)
    elif sort == "citations":
        ranked_documents = sorted(documents, key=lambda x: x.get("citations", 0), reverse=True)
    elif sort == "title":
        ranked_documents = sorted(documents, key=lambda x: x.get("title", "").lower())
    else:
        ranked_documents = sorted(documents, key=lambda x: x["score"], reverse=True)

    top_documents = [
        {"score": doc["score"], "title": doc.get("title", "Unknown Title"), "id": str(doc["_id"])}
        for doc in ranked_documents[:limit]
    ]
    return top_documents

# Endpoint untuk halaman beranda
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint untuk pencarian
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    sort = request.args.get('sort', 'relevance')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    results = search_papers(query, sort=sort)
    return jsonify(results)

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
