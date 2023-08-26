import unittest

from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet1 = Vet('Sophie Hill', 'Veterinarian', id = 1)

    def test_vet_has_name(self):
        self.assertEqual('Sophie Hill', self.vet1.name)

    def test_vet_has_position(self):
        self.assertEqual('Veterinarian', self.vet1.position)

    def test_vet_has_id(self):
        self.assertEqual(1, self.vet1.id)