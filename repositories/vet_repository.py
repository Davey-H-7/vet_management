from db.run_sql import run_sql
from models.vet import Vet
import pdb


# define function called 'save' with input parameter 'vet'
    #set variable 'sql' = sql code 'insert into vets database new data of values %s as placeholder then return new data'
    #set values = vet first_name, vet last_name and vet position to be inserted
    #set results variable = returned values of function 'run_sql' where parameters are 'sql' and 'values'
    #set variable 'id' = object in 'results' dictionary at position [0] with key 'id'
    #set id of 'vet' object = to variable 'id'
    #return vet

def save (vet):
    sql = "INSERT INTO vets (first_name,last_name, position) VALUES (%s, %s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name, vet.position]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets =[]
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['position'], row['id'])
        vets.append(vet)
    return vets

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['last_name'], result['position'], result ['id'])
    return vet

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)
