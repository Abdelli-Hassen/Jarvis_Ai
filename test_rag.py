from rag_store import RAGStore

# Sample documents
docs = [
    "Python is a programming language.",
    "Jarvis is an AI assistant.",
    "Vosk allows offline speech recognition.",
    "Coqui TTS is used for text-to-speech.",
    "Faiss is a library for fast similarity search."
]

# Create RAG store
store = RAGStore()

# Build the embeddings/index
print("Building RAG store embeddings...")
store.build(docs)

# Test retrieval
queries = [
    "Tell me about Python",
    "Who is Jarvis?",
    "Offline speech recognition library"
]

for q in queries:
    print(f"\nQuery: {q}")
    results = store.retrieve(q, top_k=2)
    for i, r in enumerate(results):
        print(f"Result {i+1}: {r}")
