import unittest

from minemoddb.models.person import Person
from minemoddb.database.person_database import PersonDatabase


class PersonDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = PersonDatabase()

    def test_db_index_begins_zeroed(self):
        self.assertEqual(self.db._index, 0)

    def test_add_person(self):
        person = Person('Juliano')
        self.db.add_person(person)
        entries = self.db.retrieve_entries()
        self.assertTrue(person in entries.values())

    def test_add_person_returns_id(self):
        person = Person('Juliano')
        person_id = self.db.add_person(person)
        self.assertEqual(person_id, 0)

    def test_remove_person(self):
        person = Person('Gabriel')
        self.db.add_person(person)
        self.db.remove_person(person)
        self.assertTrue(len(self.db.retrieve_entries()) == 0)

    def test_get_person_id(self):
        person1 = Person('Gabriel')
        self.db.add_person(person1)
        person2 = Person('Juliano')
        self.db.add_person(person2)

        actual_person1_id = self.db.get_person_id(person1)
        actual_person2_id = self.db.get_person_id(person2)
        self.assertEqual(actual_person1_id, 0)
        self.assertEqual(actual_person2_id, 1)

    def test_get_person(self):
        person = Person('Felipe')
        person_id = self.db.add_person(person)
        actual = self.db.get_person(person_id)
        self.assertEqual(actual, person)

    def test_add_person_adds_a_copy(self):
        person = Person('Type')
        person_id = self.db.add_person(person)
        person.name = 'João'
        actual = self.db.get_person(person_id)
        expected = Person('Type')
        self.assertEqual(actual, expected)

    def test_get_person_returns_a_copy(self):
        person = Person('Type')
        person_id = self.db.add_person(person)

        person_from_id = self.db.get_person(person_id)
        person_from_id.name = 'João'
        actual = self.db.get_person(person_id)
        expected = Person('Type')
        self.assertEqual(actual, expected)

    def test_modify_person(self):
        # Preparação
        person = Person('Type')
        person_id = self.db.add_person(person)

        # Asserção
        person_from_id = self.db.get_person(person_id)
        person_from_id.name = 'Novo Nome Legal'
        self.db.modify_person(person_id, person_from_id)
        expected = Person('Novo Nome Legal')
        actual = self.db.get_person(person_id)
        self.assertEqual(actual, expected)

    def test_modify_person_adds_a_copy(self):
        # Preparação
        person = Person('Type')
        person_id = self.db.add_person(person)

        # Asserção
        person_from_id = self.db.get_person(person_id)
        self.db.modify_person(person_id, person_from_id)
        person_from_id.name = 'João'
        actual = self.db.get_person(person_id)
        expected = Person('Type')
        self.assertEqual(actual, expected)
