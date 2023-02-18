import unittest
from test.test_login import TestUserLogin
from test.test_signup import TestUserSignup

def main_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestUserSignup())
    test_suite.addTest(TestUserLogin())
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(main_suite())
