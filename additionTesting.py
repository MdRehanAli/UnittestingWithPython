import unittest
from addition import additions

class additionTest(unittest.TestCase):
    def test_01(self):
        comingValues = additions(5)
        assert comingValues == 15

    def test_02(self):
        comingValues = additions(10)
        assert comingValues == 15


    def test_03(self):
        comingValues = additions(10)
        assert comingValues == 55