import unittest

from models.vet import Vet
from models.pet import Pet

class TestPet(unittest.TestCase):
    
    def setUp (self):
        self.vet1 = Vet('Sophie Hill', 'Veterinarian', id = 1)
        self.pet1 = Pet('Winnie', '5/7/2017', 'Dog', 'Malcolm Hunter', '01234 567 890', self.vet1, 'Broken tail', id = 2)

    def test_pet_has_name (self):
        self.assertEqual('Winnie', self.pet1.name)

    def test_pet_has_dob (self):
        self.assertEqual('5/7/2017', self.pet1.dob)

    def test_pet_has_species (self):
        self.assertEqual('Dog', self.pet1.species)

    def test_pet_has_owner (self):
        self.assertEqual('Malcolm Hunter', self.pet1.owner)

    def test_pet_has_contact_no (self):
        self.assertEqual('01234 567 890', self.pet1.contact_no)

    def test_pet_has_vet (self):
        self.assertEqual(self.vet1, self.pet1.vet)

    def test_pet_has_treatment_notes (self):
        self.assertEqual('Broken tail', self.pet1.treatment_notes)

    def test_pet_has_id (self):
        self.assertEqual(2, self.pet1.id)
        