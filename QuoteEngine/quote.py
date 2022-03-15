
class QuoteModel:
    def __init__(self, body: str, author: str):
        """Create a new 'QuoteModel'.

        :param body: Body of the inspirational quote.
        :param author: Name of the author, of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return ”body text” - author, a computer-readable string representation of this object."""
        return f'\"{self.body}\" - {self.author}'

    def __str__(self):
        """Return 'str(self)'."""
        return f'{self.body} - {self.author}'
