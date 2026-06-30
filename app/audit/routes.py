from flask import Blueprint, render_template
from app.decorators.auth import login_required
from app.models.audit_log import AuditLog

audit = Blueprint("audit", __name__)


@audit.route("/audit-logs")
@login_required
def audit_logs():

    logs = (
        AuditLog.query
        .order_by(AuditLog.created_at.desc())
        .all()
    )

    return render_template(
        "audit_logs.html",
        logs=logs
    )