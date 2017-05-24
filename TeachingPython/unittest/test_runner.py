import unittest

import TeachingPython.unittest_00 as post

import TeachingPython.unittest.unittest_basic as test

ASSIGNMENT = "assignment0"

students = ["fernand029", "failur029"]

# initialize the test suite
loader = unittest.TestLoader()

for student in students:
    suite = unittest.TestSuite()
    file_name = student + "_" + ASSIGNMENT
    post.TestFile.FILE_NAME = file_name

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(post))

    # initialize a runner, pass it your suite and run it
    file = open(file_name + "_results.txt", "w")
    runner = test.MyTestRunner(file)
    result = runner.run(suite)
    file.close()
