import unittest
from UnitTests.CategoriesService.CategoriesServiceTest import CategoriesServiceTest
from UnitTests.RemoteTests.Controller.LoginControllerTest import LoginControllerTest
from UnitTests.Validation.UserServiceTest import UserServiceTest

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(CategoriesServiceTest))
    test_suite.addTest(unittest.makeSuite(UserServiceTest))
    test_suite.addTest(unittest.makeSuite(LoginControllerTest))

    unittest.TextTestRunner().run(test_suite)