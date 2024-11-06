from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['research_paper_dataset']  # Nama database
collection = db['research_paper']  # Nama koleksi

# Mengambil data dari MongoDB dan menggabungkan field yang ada
documents = list(collection.find({}, {"title": 1, "abstract": 1, "_id": 1}).limit(100000))
combined_documents = [f"{doc.get('title', '')} {doc.get('abstract', '')}" for doc in documents]

# Query pencarian dari pengguna
query = "chemistry chemical interactions"

# Konversi dokumen dan query menjadi vektor TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(combined_documents + [query])

# Hitung kemiripan (cosine similarity) antara query dan setiap dokumen
similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

# Sortir dokumen berdasarkan skor kemiripan
ranked_documents = sorted(
    zip(similarity_scores, documents),
    key=lambda x: x[0],
    reverse=True
)

# Tampilkan 10 hasil pencarian teratas
print("Hasil Pencarian (Top 10):")
for score, doc in ranked_documents[:10]:  # Batasi hanya 10 hasil teratas
    print(f"Skor Kemiripan: {score:.2f} - Judul: {doc.get('title', 'Unknown Title')}, ID: {doc['_id']}")
