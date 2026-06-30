from database.db import db


class AzureConfig(db.Model):
    __tablename__ = "azure_config"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.String(255), nullable=False)
    client_secret = db.Column(db.String(500), nullable=False)

    subscription_id = db.Column(db.String(255), nullable=False)

    status = db.Column(db.String(30), default="Disconnected")