import random


"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,path):
        '''Reads words from a file and provides random word selection'''
        self.words = self.read_words_from_file(path)


    def __repr__(self):
        return f"{len(self.words)} words read"

    def read_words_from_file(self, path):
        '''Checks for empty lines and removes the trailing white spaces'''
        with open(path, "r") as file:
            words = [line.strip() for line in file if line.strip()]
        return words

    def random(self):
        """Returns a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    '''Checks and skips text that starts w/ #'''
    def read_words_from_file(self, path):
        words = super().read_words_from_file(path)
        return [word for word in words if not word.startswith("#")]
