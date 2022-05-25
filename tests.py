import unittest
from dodatak_A import OperationsManager


class TestDivisionMethods(unittest.TestCase):

    def test_basic_1(self):
        self.assertEquals(OperationsManager(1, 1).perform_division(), 1.)

    def test_basic_2(self):
        self.assertEquals(OperationsManager(1, 2).perform_division(), .5)

    def test_basic_3(self):
        self.assertEquals(OperationsManager(1, 5).perform_division(), .2)

    def test_zero_1(self):
        self.assertEquals(OperationsManager(1, 0).perform_division(), float('nan'))

    def test_zero_2(self):
        self.assertEquals(OperationsManager(1, 0.).perform_division(), float('nan'))

    def test_None_1(self):
        self.assertEquals(OperationsManager(None, 0).perform_division(), float('nan'))

    def test_None_2(self):
        self.assertEquals(OperationsManager(None, None).perform_division(), float('nan'))

    def test_List_1(self):
        self.assertEquals(OperationsManager([], 1).perform_division(), float('nan'))

    def test_List_2(self):
        self.assertEquals(OperationsManager([], []).perform_division(), float('nan'))

    def test_List_3(self):
        self.assertEquals(OperationsManager([[],[],[3,1]], [1.0]).perform_division(), float('nan'))
    def test_List_3(self):
        self.assertEquals(OperationsManager([[],[],[3,1]], [1.0]).perform_division(), float('nan'))

    def test_string_1(self):
        self.assertEquals(OperationsManager(3, "1").perform_division(), 3.)

    def test_string_2(self):
        self.assertEquals(OperationsManager(3, "-1").perform_division(), -3.)

    def test_string_3(self):
        self.assertEquals(OperationsManager("3", "3").perform_division(), 1.)

if __name__ == "__main__":
    unittest.main()
