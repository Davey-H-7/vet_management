import pdb

from models.pet import Pet
from models.vet import Vet

# import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet_repository.delete_all()

vet1 = Vet('Martha', 'Jones', 'Head Veterinarian')
vet_repository.save(vet1)
vet2 = Vet('Rose', 'Tyler', 'Junior Veterinarian')
vet_repository.save(vet2)

vets = vet_repository.select_all()

vet3 = vet_repository.select(1)


pdb.set_trace()

