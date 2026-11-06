from langchain_chroma import Chroma

from .embeddings import get_embeddings

from .vector_store import get_vector_store



def retrieve_guidelines(query, k=3):
    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )

    return retriever.invoke(query)

