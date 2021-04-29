import unittest
import ReadBytesFromFile 
# import DataFrameContextManager 

class TestInitial(unittest.TestCase):
    def setUp(self):
        self.textfile = '../files/sample.txt'
        self.tsvfile =  '../files/sample.tsv'
        self.csvfile=   '../files/sample.csv'

    def test_closed_on_exit(self):
        with ReadBytesFromFile.ContextManager(self.textfile, 'r') as f:
            f.read()
        self.assertEqual(f.closed, True)


    def tearDown(self):
        self.textfile = None
        self.tsvfile =  None
        self.csvfile=   None


if __name__ == '__main__':
    unittest.main()