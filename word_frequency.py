import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        # print(self.filename)


    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        self.filename = open(file)
        contents = self.filename.read()
        self.filename.close()
        return contents




class WordList:
    def __init__(self, text):
        self.text = text
        self.words = []

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        self.text = self.text.split()
        self.words = [word.lower().strip(string.punctuation) for word in self.text]
        

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        self.words = [word for word in self.words if word not in STOP_WORDS]

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        freqs = {}
        for item in self.words:
            freqs[item] = freqs.get(item, 0) + 1
        return freqs


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs
        self.word_freqs = []
    
    def get_second_item(self, seq):
        self.seq = seq
        return self.seq[1]

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        self.word_freqs = sorted(self.word_freqs.items(),
        key= self.seq,
        reverse=True)
        words_to_display = [freq[0] for freq in self.freqs[:10]]
        longest_word_length = max([len(word) for word in words_to_display])
        for word, count in self.freqs[:10]:
            print(word.rjust(longest_word_length + 1), "|",
              str(count).ljust(4), "*" * count)


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
