import unittest

from models.owner import Owner

class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner('Carol', 'Hill', '05678 345 222', id = 4)

    def test_owner_has_first_name(self):
        self.assertEqual('Carol', self.owner.first_name)

    def test_owner_has_last_name(self):
        self.assertEqual('Hill', self.owner.last_name)

    def test_owner_has_contact_no(self):
        self.assertEqual('05678 345 222', self.owner.contact_no)

    def test_owner_has_id(self):
        self.assertEqual(4, self.owner.id)