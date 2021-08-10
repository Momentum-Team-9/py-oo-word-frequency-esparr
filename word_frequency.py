from io import TextIOWrapper


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        file = open(self.filename)
        text = file.readlines()
        return text
        # raise NotImplementedError("FileReader.read_contents")

class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        import string
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        text = self.text
        text = str(text).replace("\\n", "")
        result = ""
        for i in text:
            if i not in string.punctuation:
                result += i
        result = str(result).lower().split(" ")
        self.text = result
        return self.text
        # raise NotImplementedError("WordList.extract_words")

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        text = self.text
        stop_word_set = set(STOP_WORDS)
        self.text = [item for item in text if item not in stop_word_set]
        return self.text
        
        # raise NotImplementedError("WordList.remove_stop_words")

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        text = self.text
        word_count = {}

        for i in text:
            if i not in word_count:
                for i in text:
                    word_count[i] = text.count(i)

        self.freqs = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        return self.freqs
        # raise NotImplementedError("WordList.get_freqs")


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

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
        freqs = self.freqs
        freqs = dict(list(freqs.items())[1:10])
        for key, value in freqs.items():
            print(str(key).rjust(15), ' | ', str(value).center(2), value * ('*'))
        # raise NotImplementedError("FreqPrinter.print_freqs")


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
