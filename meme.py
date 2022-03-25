""" An engine which provides a CLI for interacting with the meme generator. """

import os
import random
from argparse import ArgumentParser

from Ingestors import Ingestor
from QuoteEngine import MemeEngine, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote. """
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./Memes_CLI')
    path = meme.make_meme(img, quote.body, quote.author)

    return path


if __name__ == '__main__':
    parser = ArgumentParser(description='Generate a meme!')
    parser.add_argument('--path', type=str, required=False, nargs='?',
                        default=None, help='Path to the image.')
    parser.add_argument('--body', type=str, required=False, nargs='?',
                        default=None, help='Body of the quote.')
    parser.add_argument('--author', type=str, required=False, nargs='?',
                        default=None, help='Author of the quote.')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
