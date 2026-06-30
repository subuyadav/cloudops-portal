from datetime import datetime
from database.db import db


class AuditLog(db.Model):

    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), nullable=False)

    action = db.Column(db.String(255), nullable=False)

    module = db.Column(db.String(100), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )