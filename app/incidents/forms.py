from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class IncidentForm(FlaskForm):

    title = StringField(
        "Incident Title",
        validators=[DataRequired()]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )

    priority = SelectField(
        "Priority",
        choices=[
            ("Critical", "Critical"),
            ("High", "High"),
            ("Medium", "Medium"),
            ("Low", "Low")
        ]
    )

    status = SelectField(
        "Status",
        choices=[
            ("Open", "Open"),
            ("In Progress", "In Progress"),
            ("Resolved", "Resolved"),
            ("Closed", "Closed")
        ]
    )

    assigned_to = StringField("Assigned To")

    submit = SubmitField("Save Incident")