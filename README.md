# ChromaDB Semantic Product Search

## Overview

This project converts a collection of product information stored in JSON format into a searchable semantic database using ChromaDB.

Unlike traditional keyword search, this project uses vector embeddings to search by **meaning**. A user can enter natural language queries such as:

* "hydrates dry hair"
* "vitamin c serum"
* "products for damaged hair"

and receive the most semantically relevant products from the dataset.

---

## Features

* Loads product information from a JSON file.
* Recursively processes nested dictionaries and lists into searchable documents.
* Stores product metadata separately from document text.
* Creates a ChromaDB collection in memory.
* Performs semantic search using natural language queries.
* Interactive command-line interface for testing searches.

---

## Utility Functions

### `output_test_file()`

This function is used for debugging and testing.

It accepts any Python data type (such as lists, dictionaries, or strings) and converts it into readable text using the recursive helper functions before writing the output to `testing.txt`.

This allows the generated documents and metadata to be inspected without printing large amounts of information to the console.

Example use cases include:

* Verifying generated documents before adding them to ChromaDB.
* Inspecting nested JSON structures after processing.
* Debugging recursive parsing functions.

---

### `Testing()`

This function provides an interactive command-line interface for querying the ChromaDB collection.

Workflow:

1. Prompts the user to enter a natural language search query.
2. Allows the user to specify how many results should be returned.
3. Performs a semantic search using `collection.query()`.
4. Prints the matching documents.
5. Returns `True` to continue the testing loop or exits when the user enters `exit`.

This function is intended as a simple testing utility to evaluate how well the semantic search performs with different user queries.


## Project Structure

```text
.
├── data/
│   └── Product Information.json
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. Load JSON

The program reads the product dataset from:

```text
data/Product Information.json
```

---

### 2. Convert JSON into Documents

Because the dataset contains nested dictionaries and lists, two recursive helper functions are used:

* `loop_dictionary()`
* `loop_lists()`

These functions flatten the JSON into readable text that can be embedded by ChromaDB.

For example, a nested product becomes a document containing information such as:

* Product name
* Ingredients
* Product details
* Recommended usage
* Additional attributes

---

### 3. Build Metadata

Alongside each document, metadata is stored separately.

Example metadata includes:

* Product name
* Ingredients
* Recommended uses
* Product details

Metadata can later be used for filtering or displaying product information.

---

### 4. Create a ChromaDB Collection

The processed documents are inserted into a ChromaDB collection together with their metadata and unique IDs.

Each document is automatically converted into vector embeddings by ChromaDB's embedding model.

---

### 5. Semantic Search

The user enters a natural language query.

Example:

```text
What r u looking for??: products for damaged hair
```

The program searches for the closest document embeddings and returns the most relevant matches.

---

## Running the Project

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

---

## Example

Input:

```text
What r u looking for??: vitamin c serum
how many?: 3
```

Output:

```text
<Most relevant product>

<Second closest product>

<Third closest product>
```

---

## Dependencies

Install with:

```bash
pip install -r requirements.txt
```

---

## Notes

* Documents are generated recursively from nested JSON structures.
* The database is currently stored in memory and is recreated each time the program runs.
* Semantic search returns products based on meaning rather than exact keyword matches.
* A helper function (`output_test_file`) is included for debugging generated documents.

---
