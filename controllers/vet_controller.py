from flask import Flask, render_template, Blueprint, redirect
import repositories.vet_repository as vet_repository
from models.vet import Vet

vet_blueprint = Blueprint('vet', __name__)


