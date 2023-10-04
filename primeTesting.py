import unittest
from prime import isPrimeOrNot
class PrimeTest(unittest.TestCase):
    def test_1(self):
        comingValue = isPrimeOrNot(10)
        assert comingValue == True

    def test_2(self):
        comingValue = isPrimeOrNot(17)
        assert comingValue == True

    def test_3(self):
        comingValue = isPrimeOrNot(19)
        assert comingValue == True

    def test_4(self):
        comingValue = isPrimeOrNot(20)
        assert comingValue == True
