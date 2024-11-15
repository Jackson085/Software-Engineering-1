import unittest
from UnitTests.CategoriesService.CategoriesServiceTest import CategoriesServiceTest
from UnitTests.Validation.UserServiceTest import UserServiceTest

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(CategoriesServiceTest))
    test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(UserServiceTest))

    unittest.TextTestRunner().run(test_suite)