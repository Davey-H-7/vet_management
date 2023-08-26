from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository
import pdb

def save (pet):
    sql = "INSERT INTO pets (name, dob, species, owner, contact_no, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.dob, pet.species, pet.owner, pet.contact_no, pet.vet.id, pet.treatment_notes]
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
        pet = Pet(row['name'], row['dob'], row['species'], row['owner'], row['contact_no'], vet, row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)