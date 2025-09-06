# rag_store.py
from sentence_transformers import SentenceTransformer
import numpy as np
import os, pickle

# prefer faiss for speed; fallback to sklearn if faiss not available
USE_FAISS = True
try:
    import faiss
except Exception:
    USE_FAISS = False
    from sklearn.neighbors import NearestNeighbors

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

class RAGStore:
    def __init__(self, embed_model_name=EMBED_MODEL):
        self.embed = SentenceTransformer(embed_model_name)
        self.index = None
        self.docs = []

    def build(self, docs):
        """docs: list of strings"""
        self.docs = docs
        embs = self.embed.encode(docs, convert_to_numpy=True, show_progress_bar=True)
        self.dim = embs.shape[1]
        if USE_FAISS:
            self.index = faiss.IndexFlatIP(self.dim)
            faiss.normalize_L2(embs)
            self.index.add(embs)
            self.embs = embs
        else:
            # sklearn fallback (cosine via normalized vectors)
            embs_norm = embs / np.linalg.norm(embs, axis=1, keepdims=True)
            self.nbrs = NearestNeighbors(n_neighbors=5, metric='cosine').fit(embs_norm)
            self.embs = embs_norm

    def retrieve(self, query, top_k=3):
        qemb = self.embed.encode([query], convert_to_numpy=True)
        if USE_FAISS:
            faiss.normalize_L2(qemb)
            D, I = self.index.search(qemb, top_k)
            scores = D[0].tolist()
            idxs = I[0].tolist()
        else:
            qn = qemb / np.linalg.norm(qemb, axis=1, keepdims=True)
            dist, idxs = self.nbrs.kneighbors(qn, n_neighbors=top_k)
            scores = (1 - dist[0]).tolist()
            idxs = idxs[0].tolist()
        results = [{"doc": self.docs[i], "score": scores[idx]} for idx,i in enumerate(idxs)]
        # simpler return: list of docs
        return [self.docs[i] for i in idxs]
