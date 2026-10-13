
import json
from pathlib import Path

import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer


DATA_PATH = Path(__file__).parent / "knowledge_base.json"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(MODEL_NAME)


def load_documents():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    documents = data.get("documents", [])

    # Create consistent searchable text for each document.
    return [
        {
            **doc,
            "search_text": (
                f"Category: {doc.get('category', '')}. "
                f"{doc.get('content', '')}"
            ),
        }
        for doc in documents
    ]


@st.cache_data
def create_document_embeddings(texts):
    model = load_embedding_model()
    return model.encode(
        texts,
        normalize_embeddings=True,
        convert_to_numpy=True,
    )


def retrieve_documents(question, top_k=3, threshold=0.30):
    documents = load_documents()

    if not documents or not question.strip():
        return []

    model = load_embedding_model()

    document_texts = [doc["search_text"] for doc in documents]
    document_embeddings = create_document_embeddings(
        document_texts
    )

    query_embedding = model.encode(
        [question],
        normalize_embeddings=True,
        convert_to_numpy=True,
    )[0]

    # Normalized vectors allow dot product to measure cosine similarity.
    scores = np.dot(document_embeddings, query_embedding)

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in ranked_indices:
        score = float(scores[index])

        if score >= threshold:
            result = documents[int(index)].copy()
            result["similarity"] = round(score, 4)
            results.append(result)

    return results
