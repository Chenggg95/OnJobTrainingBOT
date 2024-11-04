#__import__("pysqlite3")
#import sys
#sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def load_and_split_document():
    print("loading document")
    embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-large-prd-gcc2-lb", openai_api_base="https://litellm.govtext.gov.sg/"
    )
    pdf_path = "document/document.pdf"
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""], chunk_size=500, chunk_overlap=50
    )

    splitted_documents = text_splitter.split_documents(pages)
    vectordb = Chroma.from_documents(
        splitted_documents, embeddings_model, collection_name="embedding_semantic", persist_directory="./vector_db"
    )

    return vectordb


def load_document():
    embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-large-prd-gcc2-lb", openai_api_base="https://litellm.govtext.gov.sg/"
    )
    pdf_path = "document/document.pdf"
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages
