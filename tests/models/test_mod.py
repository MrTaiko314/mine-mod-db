import unittest

from minemoddb.models.person import Person
from minemoddb.models.mod import Mod


class ModTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.owner = Person('Benjamin')

    def test_mod_has_name(self):
        mod = Mod('Mod bacana', self.owner)
        self.assertTrue(mod.name)

    def test_mod_has_owner(self):
        mod = Mod('Mod bacana', self.owner)
        self.assertTrue(mod.owner)

    def test_mod_is_compared_by_name_and_owner(self):
        actual = Mod('Mod legal', self.owner)
        expected = Mod('Mod legal', Person('Benjamin'))
        self.assertEqual(actual, expected)
