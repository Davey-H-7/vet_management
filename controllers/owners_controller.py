from flask import Flask, render_template, Blueprint, redirect, request
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import pdb
from models.owner import Owner

owner_blueprint = Blueprint('owner', __name__)

@owner_blueprint.route('/owners')
def index():
    owners = owner_repository.select_all()
    return render_template('owners/index.html', title = 'All Pet Owners', all_owners = owners)

@owner_blueprint.route('/owners/<id>')
def show (id):
    owner = owner_repository.select(id)
    pets = pet_repository.pets_for_owner(owner)
    return render_template('owners/show.html', title = owner.first_name, owner = owner, pets = pets)

@owner_blueprint.route('/owners/new')
def new_owner():
    return render_template('owners/new.html', title = 'New Pet Owner')

@owner_blueprint.route('/owners', methods =['POST'])
def save_owner():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    contact_no = request.form['contact_no']
    new_owner = Owner(first_name, last_name, contact_no)
    owner_repository.save(new_owner)
    return redirect ('/owners')

@owner_blueprint.route('/owners/<id>/edit')
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner = owner)

@owner_blueprint.route('/owners/<id>', methods =['POST'])
def update_owner(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    contact_no = request.form['contact_no']
    registered = request.form['registered']
    owner_updated = Owner(first_name, last_name, contact_no, id, registered)
    owner_repository.update(owner_updated)
    return redirect (f'/owners/{owner_updated.id}')

@owner_blueprint.route('/owners/<id>/delete', methods=['POST'])
def owner_vet(id):
    owner_repository.delete(id)
    return redirect('/owners')