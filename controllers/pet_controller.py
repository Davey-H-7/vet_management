from flask import Flask, render_template, Blueprint, redirect
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
from models.vet import Vet

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