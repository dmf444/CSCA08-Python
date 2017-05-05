import unittest
import timeout_decorator


class TestFile(unittest.TestCase):
    pass


@timeout_decorator.timeout(2)
def test_import():
    import test1


if(__name__ == "__main__"):
    # unittest.main(exit=False)
    test_import()
    print("goodbye!")