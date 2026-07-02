import chromadb
import json

docs = []
metaDatas = []
documentIds = []

##Opening and reading test data
with open("data/products.json",'r') as f:
    data = json.load(f)

##Getting data from test data and putting it in variables for collection.add
def setData():
    for i in data:
        documentIds.append(i['id'])
        docs.append(f"{i["name"]} is a {i["product_type"]} made by {i['brand']}.It belongs to the {i['category']} category.Description: {i['description']}.Skin Type: {i.get('skin_type', 'N/A')}.Hair Type: {i.get('hair_type', 'N/A')}")
        metaDatas.append(
            {"name":i["name"],
             'brand':i['brand'],
             'category':i['category'],
             'product_type':i['product_type'],
             'price':i['price']
             })

setData()

##running chromadb client(on memory)
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="googoogaagas")

collection.add(
    documents = docs,
    metadatas = metaDatas,
    ids = documentIds
)

 ##Actual testing function

def Testing():
    query = input("What r u looking for??: ")

    if query=='exit':
        return 0

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    for x in results['ids']:
        print(x, end='\n\n')
    
    return 1

##Testing loop
while Testing() != 0:pass