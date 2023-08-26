import pdb

from models.pet import Pet
from models.vet import Vet

# import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet1 = Vet("Martha Jones", "Heat Veterinarian")
vet_repository.save(vet1)
vet2 = Vet('Rose Tyler', 'Junior Veterinarian')
vet_repository.save(vet2)




pdb.set_trace()

