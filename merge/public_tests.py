import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
merge = getattr(undertest, 'merge', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [3,7,9,11,14]
        l2 = [2,4,10,11,13,19,21,43]
        assert merge(l1,l2) == [2,3,4,7,9,10,11,11,13,14,19,21,43]
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
