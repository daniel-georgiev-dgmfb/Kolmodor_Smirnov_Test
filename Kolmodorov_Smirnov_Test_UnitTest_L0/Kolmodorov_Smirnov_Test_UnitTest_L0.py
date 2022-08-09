
from logging import Logger
from Kolmodor_Smirnov_Test import TestForNormality
import unittest

class KS_Tests(unittest.TestCase):
    def test_A(self):
        #Arrange
        input = [1,2,3,4,5,6];
        logger = Logger()
        test = TestForNormality(logger)
        #Execute
        #Assert
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()