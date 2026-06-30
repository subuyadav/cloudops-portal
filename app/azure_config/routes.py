from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.decorators.auth import login_required
from database.db import db
from app.models.azure_config import AzureConfig

azure_config = Blueprint("azure_config", __name__)


@azure_config.route("/azure-config", methods=["GET", "POST"])
@login_required
def azure_configuration():

    config = AzureConfig.query.first()

    if request.method == "POST":

        tenant_id = request.form["tenant_id"]
        client_id = request.form["client_id"]
        client_secret = request.form["client_secret"]
        subscription_id = request.form["subscription_id"]

        if config:

            config.tenant_id = tenant_id
            config.client_id = client_id
            config.client_secret = client_secret
            config.subscription_id = subscription_id
            config.status = "Configured"

        else:

            config = AzureConfig(
                tenant_id=tenant_id,
                client_id=client_id,
                client_secret=client_secret,
                subscription_id=subscription_id,
                status="Configured"
            )

            db.session.add(config)

        db.session.commit()

        flash("Azure configuration saved successfully.", "success")

        return redirect(url_for("azure_config.azure_configuration"))

    return render_template(
        "azure_config.html",
        config=config
    )