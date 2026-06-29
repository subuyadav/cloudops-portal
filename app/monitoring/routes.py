from flask import Blueprint, render_template
import random

monitoring = Blueprint("monitoring", __name__)


@monitoring.route("/monitoring")
def monitoring_dashboard():

    data = {
        "cpu": random.randint(15, 85),
        "memory": random.randint(30, 95),
        "disk": random.randint(25, 90),
        "network": random.randint(10, 100),
        "healthy_servers": 14,
        "critical_servers": 1,
        "warning_servers": 2
    }

    return render_template(
        "monitoring.html",
        data=data
    )