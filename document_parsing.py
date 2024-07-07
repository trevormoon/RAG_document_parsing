from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.schema.runnable import RunnablePassthrough

loader=PyPDFLoader("/파일위치")
pages=loader.load_and_split()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
texts=text.splitter.split_document