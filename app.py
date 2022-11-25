from flask import Flask

app = Flask(__name__)

from .urls import data_gen_blueprint

app.register_blueprint(data_gen_blueprint)