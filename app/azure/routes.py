from flask import Blueprint, render_template

azure = Blueprint("azure", __name__)


@azure.route("/azure")
def azure_dashboard():

    resources = {

        "virtual_machines": 18,

        "aks_clusters": 3,

        "storage_accounts": 12,

        "postgres_servers": 4,

        "key_vaults": 2,

        "app_gateways": 2,

        "load_balancers": 3,

        "virtual_networks": 6

    }

    return render_template(
        "azure_dashboard.html",
        resources=resources
    )