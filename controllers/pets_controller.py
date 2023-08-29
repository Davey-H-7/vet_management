from flask import Flask, render_template, Blueprint, redirect, request
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
from models.pet import Pet

pet_blueprint = Blueprint('pet', __name__)

@pet_blueprint.route('/pets')
def index():
    pets = pet_repository.select_all()
    return render_template('pets/index.html', title = 'Registered Pets', all_pets = pets)

@pet_blueprint.route('/pets/<id>')
def show (id):
    pet = pet_repository.select(id)
    vet = vet_repository.vet_for_pet(pet)
    owner = owner_repository.owner_for_pet(pet)
    return render_template('pets/show.html', title = pet.name, vet = vet, pet = pet, owner = owner)

@pet_blueprint.route('/pets/new')
def add_pet():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('pets/new.html', title = 'Register New Pet', all_vets = vets, all_owners = owners)

@pet_blueprint.route('/pets', methods =['POST'])
def save_pet():
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    new_pet = Pet(name, dob, species, owner, vet, treatment_notes)
    pet_repository.save(new_pet)
    return redirect ('/pets')

@pet_blueprint.route('/pets/<id>/edit')
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template('pets/edit.html', pet = pet, all_vets = vets, all_owners = owners)

@pet_blueprint.route('/pets/<id>', methods =['POST'])
def update_pet(id):
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    owner_id = request.form['owner_id']
    owner =owner_repository.select(owner_id)
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    pet = Pet(name, dob, species, owner, vet, treatment_notes, id)
    pet_repository.update(pet)
    return redirect (f'/pets/{pet.id}')

@pet_blueprint.route('/pets/<id>/delete', methods =['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')