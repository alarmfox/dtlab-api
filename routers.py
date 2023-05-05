from flask import Blueprint

router_blueprint = Blueprint('routers', __name__)

@router_blueprint.route('', methods=['GET'])
def example() -> str:
    return 'router endpoint test'
