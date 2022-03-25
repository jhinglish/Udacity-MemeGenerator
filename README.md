# Meme Generator :framed_picture:

###### A custom meme generator, which allows for interface through your localhost (web) or CLI. Udacity Intermediate Python Nanodegree Capstone Project.

_____

# Setup
- Install dependencies using `pip install -r requirements.txt`.

##### Web Interface
1. Run 
```
export FLASK_APP=app.py
flask run --host localhost --port 3000 --reload
```
2. Navigate to [https://localhost:3000](https://localhost:3000) in your browser.
3. Generate your custom memes!

#### Web App Features
- Navigate to [https://localhost:3000](https://localhost:3000) in your browser.
- Randomly generate memes. These will be stored in `./Memes_Web`.
- Custom memes can also be generated after inputting the relevant information, by clicking on "Create".

#### Command Line Interface (CLI) Features
Via your terminal: 
- Run `python meme.py`.
  - This will generate a random meme using a random image from `./_data/photos/dog/` and a random quote from one of the files in `./_data/DogQuotes/`.
  - Quotes and images may be edited/added in the relevant folders, and memes will be randomly generated accordingly.
  - Memes will be stored in `./Memes_CLI`.
- Running `python meme.py` with these optional parameters will allow for further customization.
  - Using `--path <path/to/image>` will allow for a specific image to be used.
  - Using `--body "Insert quote here" --author "Name"` will allow for a custom quote and author to be added to the image.
    - **Note: `--body` and `--author` are required together. Inserting only one of these parameters will result in an error.**
- *Example:* `python meme.py --path ./_data/photos/dog/corgi.jpg --body "Python is fun!" --author "Jonathan Hing"`.

_____

# Modules and Sub-Modules
Arguments for the CLI and Web App can be found [here](#Setup).

##### meme.py
- This is the CLI engine for generating random or custom memes.

##### app.py
- This contains the code for web app, run with Flask, to interact with the meme generator. 

##### Ingestors
- The sub-modules found here contain the code to ingest and parse the quotes, along with their authors. The allowed extensions for files which can contain this information can be found in [ingest-interface.py](./QuoteEngine/ingest_interface.py).
  - The currently allowed file extensions are `'csv', 'docx', 'pdf', 'txt'`.

##### QuoteEngine
- These sub-modules contain the classes and functions to handle the quotes and images.
  - [meme_engine.py](./QuoteEngine/meme_engine.py) applies the font (eg. [LilitaOne-Regular](./_data/fonts/LilitaOne-Regular.ttf)) on line 40. This can be changed once the relevant file has been added to `./_data/fonts`.

_____

# Authors
##### :bust_in_silhouette: Jonathan Hing
- Github: [@Jhinglish](https://github.com/jhinglish)
- LinkedIn: [Jonathan hing](https://www.linkedin.com/in/jonathan-hing-87693665)

_____

# Contributors :sparkles:

- Sample [data](./_data) for quotes and images, as well as [html templates](./templates) provided by Udacity.
- [LilitaOne-Regular.ttf](https://fonts.google.com/specimen/Lilita+One) font.
