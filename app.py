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
def search_papers(query, limit=10):
    # Ambil 100.000 dokumen untuk analisis (bisa diubah sesuai kebutuhan)
    documents = list(collection.find({}, {"title": 1, "abstract": 1, "_id": 1}).limit(100000))
    combined_documents = [f"{doc.get('title', '')} {doc.get('abstract', '')}" for doc in documents]

    # Konversi dokumen dan query ke vektor TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_documents + [query])

    # Hitung kemiripan antara query dan setiap dokumen
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Sortir dokumen berdasarkan skor kemiripan
    ranked_documents = sorted(
        zip(similarity_scores, documents),
        key=lambda x: x[0],
        reverse=True
    )

    # Ambil hasil teratas sesuai batas
    top_documents = [
        {"score": score, "title": doc.get("title", "Unknown Title"), "id": str(doc["_id"])}
        for score, doc in ranked_documents[:limit]
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
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    # Panggil fungsi pencarian dengan query pengguna
    results = search_papers(query)
    return jsonify(results)

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
