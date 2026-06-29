from flask import Blueprint, render_template, redirect, url_for, flash

from database.db import db
from app.models.server import Server
from app.inventory.forms import ServerForm

inventory = Blueprint("inventory", __name__)


# ----------------------------
# Add Server
# ----------------------------
@inventory.route("/servers/add", methods=["GET", "POST"])
def add_server():

    form = ServerForm()

    if form.validate_on_submit():

        server = Server(
            server_name=form.server_name.data,
            ip_address=form.ip_address.data,
            environment=form.environment.data,
            operating_system=form.operating_system.data,
            owner=form.owner.data,
            resource_group=form.resource_group.data
        )

        db.session.add(server)
        db.session.commit()

        flash("Server Added Successfully!", "success")

        return redirect(url_for("inventory.add_server"))

    return render_template("add_server.html", form=form)


# ----------------------------
# List Servers
# ----------------------------
@inventory.route("/servers")
def list_servers():

    servers = Server.query.order_by(Server.server_name).all()

    return render_template(
        "servers.html",
        servers=servers
    )


# ----------------------------
# Edit Server
# ----------------------------
@inventory.route("/servers/edit/<int:id>", methods=["GET", "POST"])
def edit_server(id):

    server = Server.query.get_or_404(id)

    form = ServerForm(obj=server)

    if form.validate_on_submit():

        server.server_name = form.server_name.data
        server.ip_address = form.ip_address.data
        server.environment = form.environment.data
        server.operating_system = form.operating_system.data
        server.owner = form.owner.data
        server.resource_group = form.resource_group.data

        db.session.commit()

        flash("Server Updated Successfully!", "success")

        return redirect(url_for("inventory.list_servers"))

    return render_template(
        "add_server.html",
        form=form
    )


# ----------------------------
# Delete Server
# ----------------------------
@inventory.route("/servers/delete/<int:id>")
def delete_server(id):

    server = Server.query.get_or_404(id)

    db.session.delete(server)

    db.session.commit()

    flash("Server Deleted Successfully!", "success")

    return redirect(url_for("inventory.list_servers"))