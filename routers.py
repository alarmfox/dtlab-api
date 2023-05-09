import json
from flask import Blueprint, jsonify, request
from models import Router, db

router_blueprint = Blueprint('routers', __name__)

@router_blueprint.route('', methods=['POST'])
def create():
    pass

@router_blueprint.route('/<id>', methods=['GET'])
def get_all():
    pass 

@router_blueprint.route('/<id>', methods=['GET'])
def one(id: str):
    pass

# CREATE Delete router from scratch. It will be very similar to GET /<id>

@router_blueprint.route('/<id>', methods=['PUT'])
def update(id: str):
    if not id.isdigit():
        return jsonify({
            'error': 'id must be an integer'
        }), 400
    
    data: dict = request.get_json()

    # search by id
    router = Router.query.filter_by(id=int(id)).first()

    # return not found if not exists
    if router is None: 
        return jsonify({
            'error': 'not found'
        }), 404

    # update fields
    router.motd = data["motd"]
    router.hostname = data["hostname"]
    router.interfaces =  str(json.dumps(data["interfaces"]))

    # save result
    db.session.add(router)
    db.session.commit()

    return jsonify(router.serialize()), 200
