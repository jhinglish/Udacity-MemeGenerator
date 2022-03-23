from docx import Document

from typing import List

from QuoteEngine import QuoteModel, IngestorInterface


class DocxIngestor(IngestorInterface):
    """ A class to ingest .docx files. """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest extension: {path}')

        document = Document(path)
        quotes_list = []

        for para in document.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes_list.append(new_quote)

        return quotes_list
