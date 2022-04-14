import unittest

from minemoddb.models.person import Person


class PersonTestCase(unittest.TestCase):
    def test_person_has_name(self):
        person = Person('Juliano')
        self.assertTrue(person.name)

    def test_person_is_compared_by_name(self):
        actual = Person('Juliano')
        expected = Person('Juliano')
        self.assertEqual(actual, expected)

    def test_person_name_is_modifiable(self):
        actual = Person('Juliano')
        actual.name = 'Alberto'
        expected = Person('Alberto')
        self.assertEqual(actual, expected)
