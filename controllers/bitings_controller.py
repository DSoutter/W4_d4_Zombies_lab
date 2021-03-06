from flask import Blueprint, Flask, redirect, render_template, request

from models.biting import Biting
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository
import repositories.biting_repository as biting_repository



bitings_blueprint = Blueprint("bitings", __name__)

# INDEX

@bitings_blueprint.route("/bitings", __name__)
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings = bitings)

# NEW

# CREATE

# EDIT

# UPDATE

# DELETE
