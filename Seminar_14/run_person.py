import unittest
from person import Person, Employee, InvalidNameError, InvalidAgeError, InvalidIdError


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.valid_person = Person('Khanina', 'Nataliy', 'Vladimirovna', 26)

    def test_valid_person_creation(self):
        self.assertEqual(self.valid_person.age, 26)

    def test_invalid_name(self):
        with self.assertRaises(InvalidNameError):
            Person('', 'Nataliy', 'Vladimirovna', 25)

    def test_invalid_age(self):
        with self.assertRaises(InvalidAgeError):
            Person('Khanina', 'Nataliy', 'Vladimirovna', -5)

    def test_birthday(self):
        self.valid_person.birthday()
        self.assertEqual(self.valid_person.get_age(), 27)


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.valid_employee = Employee('Khanina', 'Nataliy', 'Vladimirovna', 26, 123456)

    def test_valid_employee_creation(self):
        self.assertEqual(self.valid_employee.get_level(), 21)

    def test_invalid_id(self):
        with self.assertRaises(InvalidIdError):
            Employee('Johnson', 'Bob', 'John', 40, 12345)