import firsttest
import unittest

class MyCaseTestCase(unittest.TestCase):
    def runTest(self):
        a = firsttest.MyClass() 
        assert a.add(1,2) == 3, 'ok'
        assert 1 == 1