from flask import Blueprint, jsonify, request
from models import Router, Interface, db

router_blueprint = Blueprint('routers', __name__)

@router_blueprint.route('', methods=['POST'])
def create():
    data: dict = request.get_json()

    hostname: str = data.get('hostname')
    if hostname == '' or hostname is None:
        return jsonify({
            'error': 'invalid or missing hostname'
        }), 400

    interfaces = []
    # TODO: handle if interfaces are missing
    for interface in data.get('interfaces'):
        # TODO: verify correctness of ip and netmask
        interfaces.append(Interface(
            name=interface['name'],
            ip=interface['ip'],
            netmask=interface['netmask'],
            description=interface['description'],
            active=interface['active']
        ))

    r = Router(
        hostname=hostname,
        motd=data.get('motd'),
        interfaces=interfaces,
    )
    db.session.add(r)
    db.session.commit()

    return jsonify(r.serialize()), 201


@router_blueprint.route('/<id>', methods=['DELETE'])
def delete(id: str):
    if not id.isdigit():
        return jsonify({
            'error': 'id must be an integer'
        }), 400

    r = Router.query.filter_by(id=int(id)).delete()
    db.session.commit()

    if r == 0:
        return jsonify({
            'error': 'not found'
        }), 404

    return '', 204
