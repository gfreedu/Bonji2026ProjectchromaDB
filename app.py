import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from semantic_search import build_collection

app = FastAPI(title="Bonji Product Search")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

collection = build_collection()

with open("data/Product Information.json", "r") as f:
    products = {f"product_{i}": p for i, p in enumerate(json.load(f))}


@app.get("/search")
def search(q: str, n: int = 3):
    results = collection.query(query_texts=[q], n_results=n)
    return {
        "query": q,
        "results": [
            {
                "product": products[pid],
                "distance": round(dist, 4),
            }
            for pid, dist in zip(results["ids"][0], results["distances"][0])
        ],
    }
