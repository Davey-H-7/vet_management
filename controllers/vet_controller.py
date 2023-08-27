from flask import Flask, render_template, Blueprint, redirect, request
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

@vet_blueprint.route('/vets/new')
def new_vet():
    return render_template('vets/new.html', title = 'New Veterinary Staff')

@vet_blueprint.route('/vets', methods =['POST'])
def save_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    position = request.form['position']
    new_vet = Vet(first_name, last_name, position)
    vet_repository.save(new_vet)
    return redirect ('/vets')

@vet_blueprint.route('/vets/<id>/edit')
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

@vet_blueprint.route('/vets/<id>', methods =['POST'])
def update_vet(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    position = request.form['position']
    vet_updated = Vet(first_name, last_name, position, id)
    vet_repository.update(vet_updated)
    return redirect ('/vets')

