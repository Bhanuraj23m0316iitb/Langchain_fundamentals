from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[1].metadata)

""" pypdf loader load page by page for each page of pdf you will get one document object that will content metadata and page content
for example if you have pdf which has 25 pages so you will get list of 25 document object with each object containing metdata and page content
""" 
