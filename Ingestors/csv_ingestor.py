import pandas as pd

from typing import List

from QuoteEngine import QuoteModel, IngestorInterface


class CSVIngestor(IngestorInterface):
    """ A class to ingest .csv files. """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest extension: {path}')

        df = pd.read_csv(path, header=0)
        quotes_list = [QuoteModel(row['body'], row['author'])
                       for index, row in df.iterrows()]

        return quotes_list
