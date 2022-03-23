""" A generator to produce inspirational quotes for memes. """

from PIL import Image, ImageFont, ImageDraw

import os
import random


class MemeEngine:
    def __init__(self, out_dir):
        """
        Insert inspirational quote onto image.

        :param out_dir: Directory where the image will be output to.
        """
        self.out_dir = out_dir

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

    def make_meme(self, img_path, body, author, width: int = 500) -> str:
        """
        Create meme from image, body, and author.

        :param img_path: Path where meme will be created.
        :param body: Body of the inspirational quote.
        :param author: Author of the inspirational quote.
        :param width: Width (default 500) for the meme to be created.
        :return: Path to the newly created imaged.
        """
        img = Image.open(img_path)

        width = 500 if width > 500 else width
        ratio = width / img.size[0]
        height = int(ratio * img.size[1])
        img = img.resize((width, height), Image.NEAREST)

        if body and height:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', size=20)
            font_position = random.choice(range(20, height - 40))
            draw.text((50, font_position), f'"{body}" - {author}', font=font, fill='white', stroke_fill='black')

        rand_num = random.randint(0, 1000)
        out_file = os.path.join(self.out_dir, f'./meme_{rand_num}.jpg')
        img.save(out_file, 'JPEG')

        return out_file
