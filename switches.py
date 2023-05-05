from flask import Blueprint, jsonify, request
from models import Switch, db

switches_blueprint = Blueprint('switches', __name__)


@switches_blueprint.route('', methods=['GET'])
def all() -> str:
    return jsonify([switch.serialize() for switch in Switch.query.all()])


@switches_blueprint.route('/<id>', methods=['GET'])
def one(id: str):
    if not id.isdigit():
        return jsonify({
            'error': 'id must be an integer'
        }), 400
    sw = Switch.query.filter_by(id=int(id)).first()

    if sw is None:
        return jsonify({
            'error': 'not found'
        }), 404

    return jsonify(sw.serialize())


@switches_blueprint.route('', methods=['POST'])
def create():
    data: dict = request.get_json()

    hostname: str = data.get('hostname')
    if hostname == '' or hostname is None:
        return jsonify({
            'error': 'unvalid or missing hostname'
        }), 400

    # TODO: verify correctness of ip and netmask

    sw = Switch(
        hostname=hostname,
        ip=data.get('ip'),
        netmask=data.get('netmask'),
        motd=data.get('motd')
    )
    db.session.add(sw)
    db.session.commit()

    return jsonify(sw.serialize()), 201
