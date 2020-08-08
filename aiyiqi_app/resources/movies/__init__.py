from flask import Blueprint

from aiyiqi_app import api
from resources.movies import movie

movie_bp = Blueprint('movies', __name__)

api.add_resource(movie.MovieList, '/movieList', endpoint='MovieList')
api.add_resource(movie.ppp, '/ppp', endpoint='ppp')
api.add_resource(movie.hello, '/hello', endpoint='hello')
