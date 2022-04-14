import unittest

from minemoddb.models.mod import Mod
from minemoddb.models.person import Person
from minemoddb.models.modpack import Modpack


class ModpackTestCase(unittest.TestCase):
    def setUp(self):
        mod1 = Mod('Super Mod Legal', Person('Juliano'))
        mod2 = Mod('Baita modzão', Person('Gabriel'))
        self.mods = [mod1, mod2]

    def test_modpack_has_name(self):
        owner = Person('Mambo314')
        modpack = Modpack('Baita Modpack', owner, self.mods)
        self.assertTrue(modpack.name)

    def test_modpack_has_owner(self):
        owner = Person('Mambo314')
        modpack = Modpack('Baita Modpack', owner, self.mods)
        self.assertTrue(modpack.owner)

    def test_modpack_has_mods(self):
        owner = Person('Mambo314')
        modpack = Modpack('Baita Modpack', owner, self.mods)
        self.assertTrue(modpack.mods)

    def test_modpack_is_compared_by_name_owner_and_mods(self):
        owner = Person('Mambo314')
        modpack = Modpack('Baita Modpack', owner, self.mods)

        owner2 = Person('Mambo314')
        mod1 = Mod('Baita modzão', Person('Gabriel'))
        mod2 = Mod('Super Mod Legal', Person('Juliano'))
        mods = [mod1, mod2]
        modpack2 = Modpack('Baita Modpack', owner2, mods)
        self.assertEqual(modpack, modpack2)
