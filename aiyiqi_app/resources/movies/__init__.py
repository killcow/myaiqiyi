from flask import Blueprint

from aiyiqi_app import api
from resources.movies import movie

movie_bp = Blueprint('movies', __name__)

api.add_resource(movie.MovieList, '/movieList', endpoint='movieList')
api.add_resource(movie.MoviePlay, '/moviePlay', endpoint='moviePlay')
api.add_resource(movie.ppp, '/ppp', endpoint='ppp')
api.add_resource(movie.hello, '/hello', endpoint='hello')
