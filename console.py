import pdb

from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet('Martha', 'Jones', 'Head Veterinarian')
vet_repository.save(vet1)
vet2 = Vet('Rose', 'Tyler', 'Junior Veterinarian')
vet_repository.save(vet2)
vet3 = Vet('Bill', 'Sickley', 'Exotic Animal Specialist')
vet_repository.save(vet3)

pet1 = Pet('Sid', '2013-06-05', 'Cat', 'Kay Hunter', '02346 789 908', vet1, 'old and heavy')
pet_repository.save(pet1)
pet2 = Pet('Skye', '2017-01-25', 'Dog', 'John Hill', '02346 544 726', vet2, 'No major issues')
pet_repository.save(pet2)
pet3 = Pet('Finn', '2022-08-19', 'Snake', 'Carol Hill', '02346 544 726', vet3, 'Hip transplant')
pet_repository.save(pet3)
pet4 = Pet('Percy', '2022-08-19', 'Parrot', 'James Brown', '02346 699 726', vet3, 'Cracker addiction')
pet_repository.save(pet4)

owner1 = Owner('Carol', 'Hill', '09876 455 322')
owner_repository.save(owner1)
owner2 = Owner('Malcolm', 'Hunter', '07823 567 211')
owner_repository.save(owner2)
owner3 = Owner('Donatello', ' Turtle', '01564 768 900')
owner_repository.save(owner3)

owner_repository.delete_all()
owners = owner_repository.select_all()
pdb.set_trace()

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

