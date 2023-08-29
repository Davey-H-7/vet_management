from db.run_sql import run_sql
from models.owner import Owner
import pdb

def save (owner):
    sql = "INSERT INTO owners (first_name,last_name, contact_no) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name, owner.contact_no]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners =[]
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['contact_no'], row['id'])
        owners.append(owner)
    owners.sort(key=lambda x: x.last_name)
    return owners

# def delete_all():
#     sql = "DELETE FROM vets"
#     run_sql(sql)

# def select(id):
#     vet = None
#     sql = "SELECT * FROM vets WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         vet = Vet(result['first_name'], result['last_name'], result['position'], result ['id'])
#     return vet

# def delete(id):
#     # pdb.set_trace()
#     sql = "DELETE FROM vets WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(vet):
#     sql = "UPDATE vets SET (first_name, last_name, position) = (%s, %s, %s) WHERE id = %s"
#     values =[vet.first_name, vet.last_name, vet.position, vet.id]
#     run_sql(sql, values)

# def vet_for_pet(pet):
#     if pet.vet:
#         sql = "SELECT * FROM vets where id = %s"
#         values = [pet.vet.id]
#         results =run_sql(sql, values)[0]
#         vet = Vet(results['first_name'], results['last_name'], results['position'], results['id'])
#     else:
#         vet = None
#     return vet