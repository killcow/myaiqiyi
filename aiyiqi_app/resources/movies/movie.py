from flask import render_template, jsonify
from flask_restful import Resource

from aiyiqi_app import api


class MovieList(Resource):
    """
    电影列表
    """

    def get(self):
        data = {'name': 'pxl'}
        return render_template('hello.html', **data)


class ppp(Resource):
    """
    电影列表
    """

    def get(self):
        return {'ss': 12}
