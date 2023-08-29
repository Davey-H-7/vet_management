import unittest

from models.vet import Vet


class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Sophie', 'Hill', 'Veterinarian', id = 1)

    def test_vet_has_first_name(self):
        self.assertEqual('Sophie', self.vet1.first_name)

    def test_vet_has_last_name(self):
        self.assertEqual('Hill', self.vet1.last_name)

    def test_vet_has_position(self):
        self.assertEqual('Veterinarian', self.vet1.position)

    def test_vet_has_id(self):
        self.assertEqual(1, self.vet1.id)