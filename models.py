from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

class Router(db.Model):

    __tablename__ = 'routers'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String)
    motd = db.Column(db.String)
    interfaces = db.relationship('Interface', backref='router', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'Router(id={self.id!r}, hostname={self.hostname!r})'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'hostname': self.hostname,
            'interfaces': [interface.serialize() for interface in self.interfaces]
        }

class Interface(db.Model):

    __tablename__ = 'interfaces'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ip = db.Column(db.String)
    netmask = db.Column(db.String)
    description = db.Column(db.String)

    router_id = db.Column(db.Integer, db.ForeignKey('routers.id', ondelete='CASCADE'), nullable=True)
    active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f'Interface(id={self.id!r}, address={self.address!r} netmask={self.netmask!r}) activated={self.activated!r} '

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'active': self.active,
            'ip': self.ip,
            'netmask': self.netmask            
        }

class Switch(db.Model):

    __tablename__ = 'switches'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String)

    ip = db.Column(db.String)
    netmask = db.Column(db.String)
    motd = db.Column(db.String)


    def __repr__(self):
        return f'Switch(id={self.id!r}, hostname={self.hostname!r}) ip={self.ip!r} netmask={self.netmask!r}'

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'hostname': self.hostname,
            'ip': self.ip,
            'netmask': self.netmask
        }