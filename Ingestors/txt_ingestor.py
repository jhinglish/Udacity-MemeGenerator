from typing import List

from QuoteEngine import QuoteModel, IngestorInterface


class TxtIngestor(IngestorInterface):
    """ A class to ingest .txt files. """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest extension: {path}')

        quotes_list = []

        with open(path, 'r') as file:
            lines = file.readlines()
            for quote in lines:
                parsed = quote.rstrip('\n').split(' - ')
                if len(parsed) > 1:
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes_list.append(new_quote)

        return quotes_list
