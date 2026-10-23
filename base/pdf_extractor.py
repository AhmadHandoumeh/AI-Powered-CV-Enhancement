import pymupdf

def extract_pdf_text(file):
    file.seek(0)

    with pymupdf.open(
        stream=file.read(),
        filetype="pdf"
    ) as document:

        text = "\n".join(
            page.get_text(sort=True)
            for page in document
        )

    return text.strip()