from db.run_sql import run_sql
from models.vet import Vet

def save (vet):
    sql = "INSERT INTO vets (name, position) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.position]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet