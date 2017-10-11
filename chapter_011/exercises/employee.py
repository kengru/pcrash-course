# Exercise 11-3. Creating a class and testing it.

class Employee():
    def __init__(self, first, last, salary):
        self.fullname = first.title() + ' ' + last.title()
        self.salary = salary

    def give_a_raise(self, amount = 5000):
        self.salary += amount
