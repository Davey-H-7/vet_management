from db.run_sql import run_sql
from models.vet import Vet


# define function called 'save' with input parameter 'vet'
    #set variable 'sql' = sql code 'insert into vets database new data of values %s as placeholder then return new data'
    #set values = vet name and vet position to be inserted
    #set results variable = returned values of function 'run_sql' where parameters are 'sql' and 'values'
    #set variable 'id' = object in 'results' dictionary at position [0] with key 'id'
    #set id of 'vet' object = to variable 'id'
    #return vet

def save (vet):
    sql = "INSERT INTO vets (name, position) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.position]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet