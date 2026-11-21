from typing import List
import logging

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


logger = logging.getLogger(__name__)


class DocumentSplitter:
    """
    Splits loaded PDF documents into smaller chunks
    suitable for semantic search.
    """

    def __init__(
        self,
        chunk_size: int,
        chunk_overlap: int,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],

            length_function=len,

            is_separator_regex=False

        )

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Split PDF pages into smaller chunks.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        logger.info("Splitting documents into chunks...")

        chunks = self.text_splitter.split_documents(
            documents
        )

        logger.info(
            f"Created {len(chunks)} chunks."
        )

        return chunks