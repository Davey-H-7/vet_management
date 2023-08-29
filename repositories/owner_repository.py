from db.run_sql import run_sql
from models.owner import Owner
import pdb

def save (owner):
    sql = "INSERT INTO owners (first_name,last_name, contact_no, registered) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name, owner.contact_no, owner.registered]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners =[]
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['contact_no'], row['id'], row['registered'])
        owners.append(owner)
    owners.sort(key=lambda x: x.last_name)
    return owners

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def select(id):
    # pdb.set_trace()
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        owner = Owner(result['first_name'], result['last_name'], result['contact_no'], result ['id'], result['registered'])
    return owner

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, contact_no, registered) = (%s, %s, %s, %s) WHERE id = %s"
    values =[owner.first_name, owner.last_name, owner.contact_no, owner.registered, owner.id]
    run_sql(sql, values)

def owner_for_pet(pet):
        # pdb.set_trace()
        sql = "SELECT * FROM owners where id = %s"
        values = [pet.owner.id]
        results =run_sql(sql, values)[0]
        owner = Owner(results['first_name'], results['last_name'], results['contact_no'], results['id'], results['registered'])
        return owner