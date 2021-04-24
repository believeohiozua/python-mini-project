import collections
import operator
import re


class SentenceCleaner:
    '''
    This class inherits the ScrapeWebsite 
    then cleans filter / cleans the text to machineable string
    and then returns a zip of the top 7 words and the counts from the website
    '''
    def __init__(self, text):
        self.text = text

    def sentence_cleaner(self):
        if self.text != 'Invalid url':
            sentence_to_dict = collections.Counter(" ".join(re.split('\W+', 
             ''.join(i for i in self.text if not i.isdigit()))).split()) 
            words, count = zip(*sorted(sentence_to_dict.items(),
            key=operator.itemgetter(1),
            reverse=True)[:7])

            return words, count
        else:
            return None