import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="googoogaagas")

collection.add(
    documents=["A small furry animal that is very stupid and keeps making bad decisions.",
    "A hairless animal that is very intelligent and solves difficult problems."],
    metadatas=[
        {'weight':'light','fur':True},
        {'weight':'heavy','fur':False}  
        ],
    ids=['stupid1','stupid2']
)

results = collection.query(
    query_texts=['furless','without fur','bald'],
    n_results=1
)

print('\n The results are:',results)