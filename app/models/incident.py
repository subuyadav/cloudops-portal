from database.db import db


class Incident(db.Model):

    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    priority = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(20), default="Open")

    assigned_to = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, server_default=db.func.now())