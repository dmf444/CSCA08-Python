import unittest
import warnings
from threading import Thread
import functools
import time
from unittest import TestProgram
from unittest import registerResult


def get_passes(unittester):
    return unittester.result.testsRun + (-len(unittester.result.errors) - len(unittester.result.failures))


def get_runs(unittester):
    return unittester.result.testsRun


def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]

            def newfunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception:
                    res[0] = Exception
            t = Thread(target=newfunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception:
                print('error starting thread')
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco


class MyTestResult(unittest._TextTestResult):

    counterz = 1

    def startTest(self, test):
        super(unittest._TextTestResult, self).startTest(test)
        self.stream.write(str(self.counterz) + ") " + self.getDescription(test)[self.getDescription(test).find(")") + 2:])
        self.stream.write("\t\t\t\t")
        self.stream.write(" ... ")
        self.stream.flush()
        self.counterz += 1

    def addSuccess(self, test):
        self.stream.writeln("ok!")

    def addError(self, test, err):
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self.stream.write("failed!")
        self.stream.write("\n")
        self.stream.flush()

    def addFailure(self, test, err):
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self.stream.write("failed!")
        self.stream.write("\n")
        self.stream.flush()


class MyTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return MyTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals
        with warnings.catch_warnings():
            if self.warnings:
                # if self.warnings is set, use it to filter all the warnings
                warnings.simplefilter(self.warnings)
                # if the filter is 'default' or 'always', special-case the
                # warnings from the deprecated unittest methods to show them
                # no more than once per module, because they can be fairly
                # noisy.  The -Wd and -Wa flags can be used to bypass this
                # only when self.warnings is None.
                if self.warnings in ['default', 'always']:
                    warnings.filterwarnings('module',
                                            category=DeprecationWarning,
                                            message='Please use assert\w+ instead.')
            startTime = time.time()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
            try:
                test(result)
            finally:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        if hasattr(result, 'separator2'):
            self.stream.writeln(result.separator2)
        run = result.testsRun
        self.stream.writeln("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", timeTaken))
        self.stream.writeln()

        expectedFails = unexpectedSuccesses = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses,
                                result.skipped))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped = results

        infos = []
        self.stream.writeln("Summary of Results: %s of %s tests successfully passed" % (run + (-len(result.errors) - len(result.failures)), run))
        self.stream.write("\n")

        return result

