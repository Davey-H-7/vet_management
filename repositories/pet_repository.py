from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

def save (pet):
    sql = "INSERT INTO pets (name, dob, species, owner_id, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.dob, pet.species, pet.owner.id, pet.vet.id, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets =[]
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], row['dob'], row['species'], owner, vet, row['treatment_notes'], row['id'])
        pets.append(pet)
    pets.sort(key=lambda x: x.name)
    return pets

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

# def select(id):
#     pet = None
#     sql = "SELECT * FROM pets WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         vet = vet_repository.select(result['vet_id'])
#         pet = Pet(result['name'], result['dob'], result['species'], result['owner'], result['contact_no'], vet, result['treatment_notes'], result ['id'])
#     return pet

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values =[id]
    run_sql(sql, values)

# def update(pet):
#     sql = "UPDATE pets SET (name, dob, species, owner, contact_no, vet_id, treatment_notes) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
#     values =[pet.name, pet.dob, pet.species, pet.owner, pet.contact_no, pet.vet.id, pet.treatment_notes, pet.id]
#     run_sql(sql, values)

# def pets_for_vet(vet):
#     # pdb.set_trace()
#     pets = []
#     sql = "SELECT * FROM pets WHERE vet_id = %s"
#     values =[vet.id]
#     results = run_sql(sql, values)

#     for row in results:
#         pet = Pet(row['name'], row['dob'], row['species'], row['owner'], row['contact_no'], vet, row['treatment_notes'], row['id'])
#         pets.append(pet)
#     return pets

# def pets_for_owner(owner):
#     # pdb.set_trace()
#     pets = []
#     sql = "SELECT * FROM pets WHERE owner_id = %s"
#     values =[owner.id]
#     results = run_sql(sql, values)

#     for row in results:
#         vet = vet_repository.select(pet.vet.id)
#         pet = Pet(row['name'], row['dob'], row['species'], row['owner'], row['contact_no'], vet, row['treatment_notes'], row['id'])
#         pets.append(pet)
#     return pets