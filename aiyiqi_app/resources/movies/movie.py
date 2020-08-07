from flask import render_template, jsonify, make_response
from flask_restful import Resource

from models.movie import CategoryMovie


class MovieList(Resource):
    """
    电影列表
    """

    def get(self):
        data = {'name': 'pxl'}
        cates = CategoryMovie.query.all()
        return render_template('hello.html', **data)


class ppp(Resource):
    """
    电影列表
    """

    def get(self):
        cates = CategoryMovie.query.all()
        return render_template('cate.html', cates=cates)
