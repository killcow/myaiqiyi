import sys

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'commons'))

from flask import Flask
from flask_restful import Api
from settings import myconfig
from utils import ov_resp


def create_app(config, env_config_file=False):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config)

    if env_config_file:
        app.config.from_envvar('str', silent=True)

    return app


app = create_app(myconfig.DevelopmentConfig)
api = Api(app)
# REPRESENTATIONS = [('application/json', ov_resp.output_json), ('text/html', ov_resp.output_html)]
# api.representations = OrderedDict(REPRESENTATIONS)
api.representation('text/html')(ov_resp.output_html)
# api.representation('application/json')(ov_resp.output_json)
