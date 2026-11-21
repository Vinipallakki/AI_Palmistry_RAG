import logging

from langchain_community.vectorstores import FAISS

from config.settings import TOP_K_RESULTS


logger = logging.getLogger(__name__)


class RetrieverManager:
    """
    Creates a retriever from the FAISS vector database.
    """

    def __init__(self, vectorstore: FAISS):

        self.vectorstore = vectorstore

    def get_retriever(self):

        logger.info("Initializing Retriever...")

        retriever = self.vectorstore.as_retriever(

            search_type="similarity",

            search_kwargs={
                "k": TOP_K_RESULTS
            }

        )

        logger.info("Retriever initialized successfully.")

        return retriever