from flask import Blueprint

switches_blueprint = Blueprint('switches', __name__)

@switches_blueprint.route('', methods=['GET'])
def example() -> str:
    return 'switch endpoint test'
