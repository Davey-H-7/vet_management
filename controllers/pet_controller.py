from flask import Flask, render_template, Blueprint, redirect, request
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
from models.vet import Vet
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
    return render_template('pets/show.html', title = pet.name, vet = vet, pet = pet)

@pet_blueprint.route('/pets/new')
def add_pet():
    vets = vet_repository.select_all()
    return render_template('pets/new.html', title = 'Register New Pet', all_vets = vets)

@pet_blueprint.route('/pets', methods =['POST'])
def save_pet():
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    owner = request.form['owner']
    contact_no = request.form['contact_no']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    new_pet = Pet(name, dob, species, owner, contact_no, vet, treatment_notes)
    pet_repository.save(new_pet)
    return redirect ('/pets')