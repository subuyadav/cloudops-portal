from flask import Blueprint, render_template, session

from app.decorators.auth import login_required
from app.models.server import Server

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def dashboard_home():

    username = session.get("username")

    total_servers = Server.query.count()

    linux_servers = Server.query.filter(
        Server.operating_system.in_(["Linux", "Ubuntu"])
    ).count()

    windows_servers = Server.query.filter_by(
        operating_system="Windows"
    ).count()

    running_servers = Server.query.filter_by(
        status="Running"
    ).count()

    recent_servers = (
        Server.query.order_by(Server.id.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        username=username,
        total_servers=total_servers,
        linux_servers=linux_servers,
        windows_servers=windows_servers,
        running_servers=running_servers,
        recent_servers=recent_servers
    )