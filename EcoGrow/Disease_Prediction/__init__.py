from flask import Blueprint

disease_identification_bp = Blueprint('disease_identification', __name__ )

from . import routes