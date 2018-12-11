import unittest
from fizzbuzz import *
from mock import patch, MagicMock
from StringIO import StringIO

class FizzBuzzTest(unittest.TestCase):
    
    def test_printfizzbuzz(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print_fizzbuzz()
            self.assertEqual(fakeOutput.getvalue().strip(), '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz')

unittest.main()
