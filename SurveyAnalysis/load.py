# Luke W. Carani, created 18 August 2023.

from langchain.document_loaders import CSVLoader
from langchain.schema.document import Document
from typing import List

def load_docs(path) -> List[Document]:
    # loader = CSVLoader(
    #     file_path=path,
    #     csv_args={
    #         "fieldnames": ['EmployeeId', 'Paygrade of Servicemember', 'Years of Service', 'Marital Status', 'Number of Dependents', 'Q1', 'Q2', 'Q3']
    #     }
    # )
    loader = CSVLoader(
        file_path=path,
    )
    documents: List[Document] = loader.load()
    return documents