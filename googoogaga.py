import chromadb
import json

docs = []
metaDatas = []
documentIds = []

with open("data/products.json",'r') as f:
    data = json.load(f)

def setData():
    for i in data:
        documentIds.append(i['id'])
        docs.append(f"{i["name"]} is a {i["product_type"]} made by {i['brand']}.It belongs to the {i['category']} category.Description: {i['description']}")
        metaDatas.append(
            {"name":i["name"],
             'brand':i['brand'],
             'category':i['category'],
             'product_type':i['product_type'],
             'price':i['price']
             })

setData()

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="googoogaagas")

collection.add(
    documents = docs,
    metadatas = metaDatas,
    ids = documentIds
)

results = collection.query(
    query_texts=["hydrating skincare", "products for damaged hair", "vitamin c serum", "refreshing face mist", "Hatsune Miku", "winter hand cream", "oily hair shampoo"],
    n_results=3
)

for x in results['ids']:
    print(x, end='\n\n')