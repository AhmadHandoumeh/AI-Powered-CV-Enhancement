from pathlib import Path
from langchain_core.documents import Document



def load_knowledge_base():
    documents = []

    folder = Path(r"base/knowledge_base")
    
    for file_path in folder.rglob("*.txt"):
        print("Hello")
        
        text = file_path.read_text(encoding="utf-8")

        document = Document(
            page_content=text,
            metadata={
                "source": str(file_path),
                "category": file_path.parent.name
            }
        )

        documents.append(document)

    return documents
