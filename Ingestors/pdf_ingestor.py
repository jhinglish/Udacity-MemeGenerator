from typing import List
import os
import subprocess

from .txt_ingestor import TxtIngestor
from QuoteEngine import QuoteModel, IngestorInterface


class PDFIngestor(IngestorInterface):
    """ A class to ingest .pdf files. """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest extension: {path}')

        rendered_pdf = './pdf_to_text.txt'
        command = f'pdftotext {path} {rendered_pdf}'
        subprocess.call(command, shell=True, stderr=subprocess.STDOUT)
        quotes_list = TxtIngestor.parse(rendered_pdf)

        os.remove(rendered_pdf)

        return quotes_list
