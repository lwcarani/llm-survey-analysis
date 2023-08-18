# Luke W. Carani, created 18 August 2023.

from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone

def split_docs(documents, chunk_size=500, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

def generate_embedding(query: str, embeddings) -> List[float]:
    """Generate an embedding for a given query."""
    query_result = embeddings.embed_query(query)
    print(f"Embedding length for the query is: {len(query_result)}")
    return query_result

def get_similiar_docs(index: Pinecone, query, k=40, score=False):
    if score:
        similar_docs = index.similarity_search_with_score(query, k=k)
    else:
        similar_docs = index.similarity_search(query, k=k)
    return similar_docs


def get_answer(index: Pinecone, model_name: str, query: str):
    similar_docs = get_similiar_docs(index, query)
    llm = ChatOpenAI(model=model_name, temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=similar_docs, question=query)

    # retriever = index.as_retriever()

    # qa_stuff = RetrievalQA.from_chain_type(
    #     llm=llm,
    #     chain_type="stuff",
    #     retriever=retriever,
    #     verbose=True
    # )
    # answer = qa_stuff.run(similar_docs)


    return answer