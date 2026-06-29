from flask import Blueprint, render_template, redirect, url_for, flash

from database.db import db
from app.models.incident import Incident
from app.incidents.forms import IncidentForm

incidents = Blueprint("incidents", __name__)


# ----------------------------------
# List Incidents
# ----------------------------------
@incidents.route("/incidents")
def list_incidents():

    incident_list = Incident.query.order_by(
        Incident.created_at.desc()
    ).all()

    return render_template(
        "incidents.html",
        incidents=incident_list
    )


# ----------------------------------
# Add Incident
# ----------------------------------
@incidents.route("/incidents/add", methods=["GET", "POST"])
def add_incident():

    form = IncidentForm()

    if form.validate_on_submit():

        incident = Incident(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            status=form.status.data,
            assigned_to=form.assigned_to.data
        )

        db.session.add(incident)
        db.session.commit()

        flash("Incident Created Successfully!", "success")

        return redirect(url_for("incidents.list_incidents"))

    return render_template(
        "add_incident.html",
        form=form
    )


# ----------------------------------
# Edit Incident
# ----------------------------------
@incidents.route("/incidents/edit/<int:id>", methods=["GET", "POST"])
def edit_incident(id):

    incident = Incident.query.get_or_404(id)

    form = IncidentForm(obj=incident)

    if form.validate_on_submit():

        incident.title = form.title.data
        incident.description = form.description.data
        incident.priority = form.priority.data
        incident.status = form.status.data
        incident.assigned_to = form.assigned_to.data

        db.session.commit()

        flash("Incident Updated Successfully!", "success")

        return redirect(url_for("incidents.list_incidents"))

    return render_template(
        "add_incident.html",
        form=form
    )


# ----------------------------------
# Delete Incident
# ----------------------------------
@incidents.route("/incidents/delete/<int:id>")
def delete_incident(id):

    incident = Incident.query.get_or_404(id)

    db.session.delete(incident)

    db.session.commit()

    flash("Incident Deleted Successfully!", "success")

    return redirect(url_for("incidents.list_incidents"))