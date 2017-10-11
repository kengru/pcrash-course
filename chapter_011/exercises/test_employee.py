# Exercise 11-3. The class.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('manuel', 'rodriguez', 10000)

    def test_default_salary(self):
        salary = self.employee.salary
        self.employee.give_a_raise()
        self.assertEqual(self.employee.salary, salary + 5000)

    def test_custom_salary(self):
        salary = self.employee.salary
        self.employee.give_a_raise(250)
        self.assertEqual(self.employee.salary, salary + 250)

unittest.main()
