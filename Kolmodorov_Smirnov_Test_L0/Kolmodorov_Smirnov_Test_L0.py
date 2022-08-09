from logging import Logger
import unittest
from Kolmodorov_Smirnov_Test import KSTestForNormality;
class Test_test1(unittest.TestCase):
    def test_KSTestForNormality(self):
        #ARRANGE
        data = [1,2,3]
        logging = Logger()
        test = Kolmodorov_Smirnov_Test.KSTestForNormality(logging)
        #EXECUTE
        self.assertEqual();
        #ASSERT

if __name__ == '__main__':
    unittest.main()