import logging
from pathlib import Path

from langchain_community.vectorstores import FAISS

from config.settings import (
    PDF_PATH,
    VECTOR_DB_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from src.loader import PDFLoader
from src.splitter import DocumentSplitter
from src.embeddings import VectorStoreManager


# ==========================================================
# Logger
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# ==========================================================
# RAG Initializer
# ==========================================================

class RAGInitializer:
    """
    Creates the FAISS vector database on first run
    and loads it on subsequent runs.
    """

    def __init__(self):

        self.vector_manager = VectorStoreManager()

    def initialize(self) -> FAISS:

        vector_path = Path(VECTOR_DB_DIR)

        try:

            if vector_path.exists() and any(vector_path.iterdir()):

                logger.info(
                    "Loading existing vector database..."
                )

                return self.vector_manager.load_vectorstore()

            logger.info(
                "No vector database found."
            )

            logger.info(
                "Loading Palmistry PDF..."
            )

            loader = PDFLoader(PDF_PATH)

            documents = loader.load_documents()

            logger.info(
                f"Loaded {len(documents)} pages."
            )

            splitter = DocumentSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
            )

            chunks = splitter.split_documents(
                documents
            )

            logger.info(
                f"Generated {len(chunks)} chunks."
            )

            vectorstore = (
                self.vector_manager.create_vectorstore(
                    chunks
                )
            )

            logger.info(
                "Vector database created successfully."
            )

            return vectorstore

        except Exception as e:

            logger.exception(
                f"Initialization failed : {e}"
            )

            raise