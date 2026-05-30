from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_relevant_chunks(question, chunks, top_k=3):
    if not chunks:
        return []

    documents = chunks + [question]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    question_vector = matrix[-1]
    chunk_vectors = matrix[:-1]

    similarities = cosine_similarity(question_vector, chunk_vectors).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]

    return [chunks[i] for i in top_indices]
