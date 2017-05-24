import unittest


class TestFile(unittest.TestCase):

    FILE_NAME = ""

    @classmethod
    def setUpClass(cls):
        cls.assignment = __import__(cls.FILE_NAME)

    def test_01_power_of_three(self):
        "Check to see if this accurately makes powers of three - 2"
        x = self.assignment.power_of_three(2)
        self.assertEqual(8, x)

    def test_02_power_of_three(self):
        "Check power of three - 80"
        y = self.assignment.power_of_three(80)
        self.assertEqual(512000, y, "np")

    def test_03_power_of_three(self):
        "Check power of three=> -4"
        z = self.assignment.power_of_three(-4)
        self.assertEqual(-64, z, "this worked")

    def test_01_borg_response(self):
        "Check if the borg response works"
        a = self.assignment.borg_response("Don't Assimilate us!!")
        self.assertEqual(a, "We are the Borg. You will be assimilated. Resistance is futile.")

    def test_02_borg_response(self):
        "Resistance is not futile"
        b = self.assignment.borg_response("0010010100010001001001011")
        self.assertEqual(b, "We are the Borg. You will be assimilated. Resistance is futile.")

    def test_01_make_dmfml(self):
        "Check with handout parameters 1"
        c = self.assignment.make_dmfml("David Ferna", 98, "01/05/98", "G")
        self.assertEqual(c, "<name=David Ferna, age=98, sex=G, birthday=01/05/98>")

    def test_02_make_dmfml(self):
        "Check with random parameters 2"
        d = self.assignment.make_dmfml("George Sherman", 23, "99/93/43", "M")
        self.assertEqual(d, "<name=George Sherman, age=23, sex=M, birthday=99/93/43>")


if(__name__ == "__main__"):
    import TeachingPython.unittest.unittest_basic as test
    file = open("unittest_01_test.txt", "w")
    runner = test.MyTestRunner(file)
    p = unittest.main(exit=False, verbosity=2, testRunner=runner)
    print(test.get_runs(p))
    file.close()