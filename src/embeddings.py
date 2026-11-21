from pathlib import Path
import logging

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config.settings import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    VECTOR_DB_DIR,
)


logger = logging.getLogger(__name__)


class VectorStoreManager:
    """
    Creates, saves and loads the FAISS vector database.
    """

    def __init__(self):

        self.embedding_model = OpenAIEmbeddings(
            model=EMBEDDING_MODEL,
            api_key=OPENAI_API_KEY,
        )

        self.vector_db_path = Path(VECTOR_DB_DIR)

    def create_vectorstore(self, documents):

        logger.info("Creating FAISS Vector Database...")

        vectorstore = FAISS.from_documents(
            documents=documents,
            embedding=self.embedding_model,
        )

        vectorstore.save_local(
            str(self.vector_db_path)
        )

        logger.info("Vector Database created successfully.")

        return vectorstore

    def load_vectorstore(self):

        if not self.vector_db_path.exists():

            raise FileNotFoundError(
                "Vector database not found."
            )

        logger.info("Loading existing Vector Database...")

        return FAISS.load_local(
            folder_path=str(self.vector_db_path),
            embeddings=self.embedding_model,
            allow_dangerous_deserialization=True,
        )