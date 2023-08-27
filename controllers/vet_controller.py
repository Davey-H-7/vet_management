from flask import Flask, render_template, Blueprint, redirect
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository
from models.vet import Vet

vet_blueprint = Blueprint('vet', __name__)

@vet_blueprint.route('/vets')
def index():
    vets = vet_repository.select_all()
    return render_template('vets/index.html', title = 'Veterinarian Staff', all_vets = vets)

@vet_blueprint.route('/vets/<id>')
def show (id):
    vet = vet_repository.select(id)
    pets = pet_repository.pets_for_vet(vet)
    return render_template('vets/show.html', title = vet.first_name, vet = vet, pets = pets)
