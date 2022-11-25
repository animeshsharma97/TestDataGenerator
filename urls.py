from flask import Blueprint

from .views import GenerateDataView

data_gen_blueprint = Blueprint("data_gen_blueprint", __name__, url_prefix="/generate-data")

data_gen_blueprint.add_url_rule(
    "",
    view_func=GenerateDataView.as_view("generate_data"),
    methods=["POST"],
)