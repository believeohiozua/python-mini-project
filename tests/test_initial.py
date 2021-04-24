import unittest
import urllib.request
import collections
import re



class TestInitial(unittest.TestCase):
    '''
    Things to test for:
    1. The link inputed is valid i.e starts with http:// or https://
    2. That the link returns a valid response http 200 ok and bea
    3. Test that the defined method can convert returned strings with crude charaters to refined clean words in a list
    4. Test that the value count for each word in the list is accurate
    5. Test that a dictionary of the top seven most occuring letters are returned
    6. Test guard against error/failures
    '''

    def setUp(self):
        self.url = 'http://www.google.com'
        self.symbols = '. \ str1 + * ? str2 [ ^ ] $ ( str3) { } = ! str4  | : -'
        self.digits= 'one 1 two 2 three 3 twenty-four 24 four'
        self.words = 'one  two  three one  twenty two one four three two one'

    def test_valid_url(self):
        status_code  = urllib.request.urlopen(self.url).getcode() == 200
        self.assertEqual(status_code, True)

    def test_clean_symbols(self):
        self.assertEqual(" ".join(re.split('\W+', self.symbols )) == ' str1 str2 str3 str4 ', True)

    def test_clean_digits(self):
        self.assertEqual(''.join(i for i in self.digits if not i.isdigit()) == 'one  two  three  twenty-four  four', True)

    def test_string_to_dict(self):
        self.assertEqual(collections.Counter(self.words.split()) == {'one': 4, 'two': 3, 'three': 2, 'twenty': 1, 'four': 1}, True)

    def tearDown(self):
        self.url = None
        self.symbols = None
        self.digits= None
        self.words = None


if __name__ == '__main__':
    unittest.main()