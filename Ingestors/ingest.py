from typing import List

from QuoteEngine import QuoteModel, IngestorInterface

from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TxtIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        A class method to ingest and process files for their quotes.

        :param path: Path to the desired file containing the quotes.
        :return: List of 'QuoteModel's containing the author and body.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
