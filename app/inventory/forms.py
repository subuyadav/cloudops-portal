from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ServerForm(FlaskForm):

    server_name = StringField(
        "Server Name",
        validators=[DataRequired()]
    )

    ip_address = StringField(
        "IP Address",
        validators=[DataRequired()]
    )

    environment = SelectField(
        "Environment",
        choices=[
            ("DEV", "DEV"),
            ("UAT", "UAT"),
            ("PREPROD", "PREPROD"),
            ("PROD", "PROD")
        ]
    )

    operating_system = SelectField(
        "Operating System",
        choices=[
            ("Windows", "Windows"),
            ("Linux", "Linux"),
            ("Ubuntu", "Ubuntu")
        ]
    )

    owner = StringField("Owner")

    resource_group = StringField("Resource Group")

    submit = SubmitField("Save Server")