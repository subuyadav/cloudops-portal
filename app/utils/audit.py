from database.db import db
from app.models.audit_log import AuditLog



def log_action(username, action, module):
    """
    Save an audit record.
    """

    try:

        log = AuditLog(
            username=username,
            action=action,
            module=module
        )

        db.session.add(log)
        db.session.commit()

    except Exception as ex:

        db.session.rollback()

        print(f"Audit Log Error : {ex}")