import pdb

from models.pet import Pet
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository


vet_repository.delete_all()

vet1 = Vet('Martha', 'Jones', 'Head Veterinarian')
vet_repository.save(vet1)
vet2 = Vet('Rose', 'Tyler', 'Junior Veterinarian')
vet_repository.save(vet2)

pet1 = Pet('Sid', '05/06/2013', 'Cat', 'Kay Hunter', '02346 789 908', vet1, 'old and heavy')
pet_repository.save(pet1)
pet2 = Pet('Skye', '017/09/2019', 'Dog', 'John Hill', '02346 544 726', vet2, 'Wee fearty')
pet_repository.save(pet2)
pet3 = Pet('Finn', '04/01/2022', 'Beast', 'Carol Hill', '02346 544 726', vet2, 'Surgery undertaken to remove objects from intestines')
pet_repository.save(pet3)

# pet_repository.delete_all()
# pet_repository.delete(2)

# pet1.name = 'Molly'
# pet_repository.update(pet1)

# pets = pet_repository.select_all()

# pet4 = pet_repository.select(3)
# pdb.set_trace()

# vet3 = vet_repository.select(1)

# vet_repository.delete(1)
# vets = vet_repository.select_all()

# vet1 = Vet('Martin', 'Jones', 'Head Veterinarian')
# vet_repository.update(vet1)
# vets = vet_repository.select_all()

# vet = vet_repository.vet_for_pet(pet2)
# pet = pet_repository.pets_for_vet(vet1)


# pdb.set_trace()

