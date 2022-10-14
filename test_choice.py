import unittest

from choice import *


class MyTestCase(unittest.TestCase):
    def test_choice(self):
        key='rock' or 'paper' or 'scissors'
        wronginput='glass'
        choice=['rock','paper','scissors']
        self.assertIn(key,choice)
        self.assertNotIn(wronginput,choice)

if __name__=='__main__':
    unittest.main()