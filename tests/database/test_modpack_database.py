import unittest

from minemoddb.models.person import Person
from minemoddb.models.mod import Mod
from minemoddb.models.modpack import Modpack
from minemoddb.database.modpack_database import ModpackDatabase


class ModpackDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = ModpackDatabase()
        self.owner = Person('Robsvaldo')
        mod1 = Mod('Grappling Hook', Person('Julisberto456'))
        mod2 = Mod('Futuristic Drill', Person('Alexey Ibraimovich'))
        mod3 = Mod('Bigger Trees', Person('Lijiao Bing'))
        self.mods = [mod1, mod2, mod3]

    def test_add_modpack(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        self.db.add_modpack(modpack)
        self.assertTrue(self.db._entries[0])

    def test_add_modpack_returns_id(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)
        self.assertEqual(modpack_id, 0)

    def test_remove_modpack(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        self.db.add_modpack(modpack)
        self.db.remove_modpack(modpack)
        self.assertEqual(len(self.db._entries), 0)

    def test_get_modpack(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)

        modpack_from_id = self.db.get_modpack(modpack_id)
        self.assertEqual(modpack_from_id, modpack)

    def test_modify_modpack(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)

        modpack_from_id = self.db.get_modpack(modpack_id)
        modpack_from_id.name = 'Modpack super show'
        self.db.modify_modpack(modpack_id, modpack_from_id)
        actual = self.db.get_modpack(modpack_id)
        expected = Modpack('Modpack super show', self.owner, self.mods)
        self.assertEqual(actual, expected)

    def test_get_modpack_id(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        expected = self.db.add_modpack(modpack)

        actual = self.db.get_modpack_id(modpack)
        self.assertEqual(actual, expected)

    def test_add_modpack_as_a_copy(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)
        modpack.name = 'Modpack não tão legal'

        actual = self.db.get_modpack(modpack_id)
        expected = Modpack('Modpack legalzão', self.owner, self.mods)
        self.assertEqual(actual, expected)

    def test_get_modpack_return_a_copy(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)

        modpack_from_id = self.db.get_modpack(modpack_id)
        modpack_from_id.name = 'Modpack bem legal'
        actual = self.db.get_modpack(modpack_id)
        expected = Modpack('Modpack legalzão', self.owner, self.mods)
        self.assertEqual(actual, expected)

    def test_modify_modpack_adds_a_copy(self):
        modpack = Modpack('Modpack legalzão', self.owner, self.mods)
        modpack_id = self.db.add_modpack(modpack)

        modpack_from_id = self.db.get_modpack(modpack_id)
        modpack_from_id.name = 'Modpack bem legal'
        self.db.modify_modpack(modpack_id, modpack_from_id)
        modpack_from_id.name = 'Modpack legalzão'
        actual = self.db.get_modpack(modpack_id)
        expected = Modpack('Modpack legalzão', self.owner, self.mods)
        self.assertNotEqual(actual, expected)
