import json
from flask import Blueprint, jsonify, request
from models import Switch, db

switches_blueprint = Blueprint('switches', __name__)

@switches_blueprint.route('', methods=['POST'])
def create():
    pass

@switches_blueprint.route('/<id>', methods=['GET'])
def get_all():
    pass 

@switches_blueprint.route('/<id>', methods=['GET'])
def one(id: str):
    pass

# CREATE Delete Switch from scratch. It will be very similar to GET /<id>

@switches_blueprint.route('/<id>', methods=['PUT'])
def update():
    if not id.isdigit():
        return jsonify({
            'error': 'id must be an integer'
        }), 400
    
    data: dict = request.get_json()

    # search by id
    switch = Switch.query.filter_by(id=int(id)).first()

    # return not found if not exists
    if switch is None: 
        return jsonify({
            'error': 'not found'
        }), 404

    # update fields
    switch.motd = data["motd"]
    switch.hostname = data["hostname"]
    switch.interfaces =  str(json.dumps(data["interfaces"]))

    # save result
    db.session.add(switch)
    db.session.commit()

    return jsonify(switch.serialize()), 200
