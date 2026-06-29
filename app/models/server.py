from database.db import db


class Server(db.Model):

    __tablename__ = "servers"

    id = db.Column(db.Integer, primary_key=True)

    server_name = db.Column(db.String(100), nullable=False)

    ip_address = db.Column(db.String(50), nullable=False)

    environment = db.Column(db.String(20), nullable=False)

    operating_system = db.Column(db.String(50), nullable=False)

    status = db.Column(db.String(20), default="Running")

    owner = db.Column(db.String(100))

    resource_group = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<Server {self.server_name}>"