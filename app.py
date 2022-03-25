""" A GUI for the meme generator. """

from flask import Flask, render_template, request
import requests

import random
import os

from Ingestors import Ingestor
from QuoteEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources. """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes_list = []
    for f in quote_files:
        try:
            quotes_list.extend(Ingestor.parse(f))
        except ValueError as error:
            print(error)

    images_path = './_data/photos/dog/'
    imgs_list = []

    for filename in os.listdir(images_path):
        im = f'{images_path}/{filename}'
        imgs_list.append(im)

    return quotes_list, imgs_list


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme. """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information. """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme. """
    img = './temp_img.jpg'
    img_url = request.form.get('image_url')
    img_content = requests.get(img_url, stream=True).content

    with open(img, 'wb') as f:
        f.write(img_content)

    body = request.form.get('body', '')
    author = request.form.get('author', 'Unknown')

    path = meme.make_meme(img, body, author)
    os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
