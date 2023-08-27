from flask import Flask, render_template, Blueprint, redirect
import repositories.pet_repository as pet_repository
from models.vet import Vet

pet_blueprint = Blueprint('pet', __name__)

@pet_blueprint.route('/pets')
def index():
    pets = pet_repository.select_all
    return render_template('pets/index.html', title = 'Registered Pets', all_pets = pets)