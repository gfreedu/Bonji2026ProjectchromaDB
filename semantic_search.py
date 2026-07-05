import json
import sys
import chromadb


def flatten(value):
    if isinstance(value, dict):
        return "\n".join(f"{k}: {flatten(v)}" for k, v in value.items())
    if isinstance(value, list):
        return "\n".join(flatten(v) for v in value)
    return str(value)


def build_collection():
    with open("data/Product Information.json", "r") as f:
        products = json.load(f)

    client = chromadb.Client()
    collection = client.create_collection(name="products")

    collection.add(
        documents=[flatten(p) for p in products],
        metadatas=[{"product_name": p["product_name"]} for p in products],
        ids=[f"product_{i}" for i in range(len(products))],
    )
    return collection


def search(collection, query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)
    for rank, (meta, distance) in enumerate(
        zip(results["metadatas"][0], results["distances"][0]), start=1
    ):
        print(f"{rank}. {meta['product_name']}  (distance: {distance:.4f})")


def main():
    collection = build_collection()

    if len(sys.argv) > 1:
        search(collection, " ".join(sys.argv[1:]))
        return

    while True:
        query = input("\nSearch (or 'exit'): ").strip()
        if query.lower() == "exit":
            break
        if query:
            search(collection, query)


if __name__ == "__main__":
    main()
