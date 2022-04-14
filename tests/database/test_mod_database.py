import unittest

from minemoddb.models.mod import Mod
from minemoddb.models.person import Person
from minemoddb.database.mod_database import ModDatabase


class ModDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = ModDatabase()

    def test_db_index_begins_zeroed(self):
        self.assertEqual(self.db._index, 0)

    def test_add_mod(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)

        self.db.add_mod(mod)
        self.assertTrue(self.db._entries[0])

    def test_add_mod_returns_id(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)

        mod_id = self.db.add_mod(mod)
        self.assertEqual(mod_id, 0)

    def test_get_mod_id(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        expected = self.db.add_mod(mod)

        actual = self.db.get_mod_id(mod)
        self.assertEqual(actual, expected)

    def test_get_mod(self):
        owner = Person('Dono')
        expected = Mod('Grappling Hook', owner)
        mod_id = self.db.add_mod(expected)

        actual = self.db.get_mod(mod_id)
        self.assertEqual(actual, expected)

    def test_add_mod_adds_a_copy(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        mod_id = self.db.add_mod(mod)
        mod.name = 'Hook Grapling'

        mod_from_db_entry = self.db._entries[mod_id]
        self.assertNotEqual(mod, mod_from_db_entry)

    def test_get_mod_returns_a_copy(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        mod_id = self.db.add_mod(mod)

        mod_from_id = self.db.get_mod(mod_id)
        mod_from_id.name = 'Hookling Grap'
        mod_from_db_entry = self.db._entries[mod_id]
        self.assertNotEqual(mod_from_id, mod_from_db_entry)

    def test_modify_mod(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        mod_id = self.db.add_mod(mod)

        mod_from_id = self.db.get_mod(mod_id)
        mod_from_id.name = 'Hookling Grap'
        mod_from_id.owner = Person('Juscelino Kubitchesqui')
        self.db.modify_mod(mod_id, mod_from_id)
        expected = Mod('Hookling Grap', Person('Juscelino Kubitchesqui'))
        actual = self.db.get_mod(mod_id)
        self.assertEqual(actual, expected)

    def test_modify_mod_adds_a_copy(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        mod_id = self.db.add_mod(mod)

        mod_from_id = self.db.get_mod(mod_id)
        mod_from_id.name = 'Hookling Grap'
        self.db.modify_mod(mod_id, mod_from_id)
        mod_from_id.name = 'Grappling Hook'
        expected = Mod('Hookling Grap', Person('Dono'))
        actual = self.db.get_mod(mod_id)
        self.assertEqual(actual, expected)

    def test_remove_mod(self):
        owner = Person('Dono')
        mod = Mod('Grappling Hook', owner)
        self.db.add_mod(mod)
        self.db.remove_mod(mod)
        self.assertEqual(len(self.db._entries), 0)
