import unittest
from UnitTests.CategoriesService.CategoriesServiceTest import CategoriesServiceTest


if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(CategoriesServiceTest))

    unittest.TextTestRunner().run(test_suite)