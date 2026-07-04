import chromadb
import json
#include <im sorry if i do something stupid like putting brackets in expression or semi colons, yes i was a die hard c++ fan
#also import annoyed human noises 

#Functions looping through dictionaries and adding them to docs folder.
def loop_dictionary(dictionary, previousText):
    for key,element in dictionary.items():
        if type(element) == type({}):                                     #Check if element is a dictionary
            previousText = previousText + '\n' + key
            previousText = loop_dictionary(element,previousText)
        elif type(element) == type([]):                                   #Check if element is a list
            previousText = previousText + '\n' + key
            previousText = loop_lists(element,previousText)
        else:                                                             #Otherwise just add element  
            previousText = previousText + '\n' + key + '\n' + str(element)
    
    return previousText                                                   #Finally return the whole text as a whole document
#Function looping lists
def loop_lists(lists,previousText):
    for element in lists:
        if type(element) == type({}):                                          #Check if element of list is a dictionary
            previousText = loop_dictionary(element,previousText)
        elif type(element) == type([]):                                        #Check if element list
            previousText = loop_lists(element,previousText)
        else:
            previousText = previousText + '\n' + str(element)
    return previousText
#Function for testing any variable for example docs metadatas documentids. (put any data type in here it will be outputed in a test file)
def output_test_file(t):
    text = ''
    if type(t) == type([]):
        text = loop_lists(t,'')
    elif type(t) == type({}):
        text = loop_dictionary(t,'')
    else:
        text = str(t)

    with open("testing.txt",'a') as f:
        f.write(str(text))
    f.close()


class vector_data_base:
    def __init__(self,filePath):
        self.docs = []
        self.metaDatas = []
        self.documentIds = []
        with open(filePath,'r') as f:
            self.data = json.load(f)
        
        #running chromadb client(on memory)
        self.chroma_client = chromadb.Client()

        self.collection = self.chroma_client.create_collection(name="googoogaagas")

    def setupDataSetVariables(self):
        id_count = 0

        for element in self.data:
            id_count += 1
            self.documentIds.append('id' + str(id_count))

            self.docs.append(loop_dictionary(element,""))

            self.metaDatas.append(
                {"name":element["product_name"],
                'ingredients':loop_lists(element['full_ingredient_list'],''),
                'solves':loop_lists(element['recommended_for'],''),
                'details':loop_dictionary(element['product_details'],''),
                })
    
    def setupCollection(self):
        self.collection.add(
            documents = self.docs,
            metadatas = self.metaDatas,
            ids = self.documentIds
        )

    def searchResults(self,query,amount):
        results = self.collection.query(
            query_texts=[query],
            n_results=input(amount)
        )
    
    def testing(self):
        while True:
            query = input("What r u looking for??: ")

            if query=='exit':
                break

            results = self.collection.query(
                query_texts=[query],
                n_results=int(input("how many?: "))
            )

            for x in results['documents']:
                output_test_file(loop_lists(x))

