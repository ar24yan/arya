import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("This is setUp method.")
    def test1(self):
        print("This is test method.")
    def test2(self):
        print("This is test method.")
    def tearDown(self):
        print("This is tearDown method.")
unittest.main()