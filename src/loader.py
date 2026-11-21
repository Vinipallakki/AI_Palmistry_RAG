from pathlib import Path
from typing import List
import logging

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


logger = logging.getLogger(__name__)


class PDFLoader:
    """
    Loads PDF documents using LangChain's PyPDFLoader.
    """

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

    def load_documents(self) -> List[Document]:
        """
        Load all pages from the PDF.

        Returns:
            List[Document]
        """

        if not self.pdf_path.exists():

            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path}"
            )

        logger.info("Loading PDF...")

        loader = PyPDFLoader(str(self.pdf_path))

        documents = loader.load()

        logger.info(
            f"Loaded {len(documents)} pages successfully."
        )

        return documents