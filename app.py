from flask import Flask, render_template
from controllers.vets_controller import vet_blueprint
from controllers.pets_controller import pet_blueprint
from controllers.owners_controller import owner_blueprint

app = Flask(__name__)
app.register_blueprint(vet_blueprint)
app.register_blueprint(pet_blueprint)
app.register_blueprint(owner_blueprint)

@app.route("/")
def home():
    return render_template("index.html", title ='Home')

if __name__ == '__main__':
    app.run(debug=True)