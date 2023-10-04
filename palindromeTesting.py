import unittest
from palindrome import isPalindromicNumber

class palindromicTest(unittest.TestCase):
    def test_001(self):
        comingValues = isPalindromicNumber("1245")
        assert comingValues == False

    def test_002(self):
        comingValues = isPalindromicNumber("1245")
        assert comingValues == True

    def test_003(self):
        comingValues = isPalindromicNumber("1221")
        assert comingValues == True