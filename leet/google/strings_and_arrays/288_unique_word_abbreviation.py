import collections
from typing import List


class ValidWordAbbr:
    '''
    the proble states
    A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
    At first glance it sounds like if we have the same abbreviation for any word from dictionary
    the abbreviation is not unique

    it turned out it is not so

    example:
    dictionary = ["hello"]
    word = "hello"

    the result is True, meaning the word "hello" has unique abbreviation because dictionary contains the same word (not
    a different word)

    This also means we need to count words as well as their abbreviations

    we return True if count of word is equal count of its abbreviation. If count is different
    that means some other word has the same abbreviation

    '''

    def __init__(self, dictionary: List[str]):
        self.words = collections.defaultdict(int)
        self.abbreviation = collections.defaultdict(int)
        for word in dictionary:
            self.words[word]+=1
            lenword = len(word) - 2
            if lenword <=0:
                self.abbreviation[word]+=1
            else:
                self.abbreviation[word[:1] + str(lenword) + word[-1:]]+=1

    def isUnique(self, word: str) -> bool:
        lenword = len(word) - 2
        abbr = word
        if lenword > 0:
            abbr = word[:1] + str(lenword) + word[-1:]
        return self.words[word] == self.abbreviation[abbr]