# Luke W. Carani, created 18 August 2023.

# standard imports
import os
from dotenv import load_dotenv
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from SurveyAnalysis.load import load_docs
from SurveyAnalysis.utils import split_docs, get_similiar_docs, get_answer, generate_embedding

# load the stored environment variables
load_dotenv()

# Get the values
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")
pinecone_index_name = os.getenv("PINECONE_INDEX")

pinecone.init(
    api_key=pinecone_api_key,
    environment=pinecone_env
)

# custom imports
from SurveyAnalysis.load import load_docs

def main(query: str) -> None:
    print(query)

    # If this is the first time uploading these documents, create a new namespace, otherwise, reference old namespace
    
    # documents = load_docs('input_files/survey_data.csv')
    # print(len(documents))
    # docs = split_docs(documents)
    # print(len(docs))

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    # index: Pinecone = Pinecone.from_documents(documents=docs, embedding=embeddings, index_name=pinecone_index_name, namespace='a')
    index: Pinecone = Pinecone.from_existing_index(index_name=pinecone_index_name, embedding=embeddings, namespace='a')

    answer = get_answer(index=index, model_name=openai_model, query=query)

    print(answer)
