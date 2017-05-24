import unittest
import time

from TeachingPython.unittest_basic import MyTestRunner, timeout


class TestFile(unittest.TestCase):
    FILE_NAME = ""

    @classmethod
    def setUpClass(cls):
        # cls.assignment = __import__(cls.FILE_NAME)
        pass

    @timeout(3)
    def test_import(self):
        "Test to see if file crashes or stays in a loop"
        try:
            __import__(self.FILE_NAME)
        except Exception:
            time.sleep(4)


if(__name__ == "__main__"):
    file = open("results.txt", "w")
    runner = MyTestRunner(file)
    p = unittest.main(exit=False, verbosity=2, testRunner=runner)
    file.close()
