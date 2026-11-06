import hashlib

from langchain_text_splitters import RecursiveCharacterTextSplitter

from .knowledge_loader import load_knowledge_base
from .vector_store import get_vector_store


def ingest_knowledge_base():
    # Step 1: Load documents
    documents = load_knowledge_base()

    print(f"Loaded {len(documents)} documents.")

    if not documents:
        print("Knowledge base is empty.")
        return

    # Step 2: Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # Step 3: Generate stable IDs
    ids = []

    for chunk in chunks:
        unique_text = (
            chunk.metadata["source"]
            + "::"
            + chunk.page_content
        )

        chunk_id = hashlib.sha256(
            unique_text.encode("utf-8")
        ).hexdigest()

        ids.append(chunk_id)

    # Step 4: Embed and store
    vector_store = get_vector_store()

    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )

    print("Knowledge base ingestion completed.")