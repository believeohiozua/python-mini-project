from bs4 import BeautifulSoup
import urllib.request
from .sentencesleaner import SentenceCleaner


class Webscrapper(SentenceCleaner): 
    '''
    This class scrapes a website using the beautiful soup library
    and then returns texts from the website
    '''   
    def __init__(self, url, cleaner=SentenceCleaner):
        self.url = url        
        self.cleaner = cleaner   
        
    def text_generator(self):
        html = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(html, features='html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        word_dict = self.cleaner(soup.getText()).sentence_cleaner()
        if word_dict is not None:
            return word_dict
        else:        
            return None
