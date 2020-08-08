from flask import render_template, jsonify
from flask_restful import Resource
from sqlalchemy import text

from models.movie import CategoryMovie, MovieTable
from models import db_session


class MovieList(Resource):
    """
    电影列表
    """

    def get(self):
        stmt = text(
            "SELECT categroy,group_concat(numid) FROM categroyMovieTable GROUP BY categroy ORDER BY categroy DESC")
        groups = db_session.execute(stmt).fetchall()

        all_list = []
        for group in groups:
            dict1 = {'group_name': group[0], 'child': []}
            numids = group[1].split(sep=',')
            for numid in numids:
                cate = CategoryMovie.query.filter_by(numid=numid).first()
                dict1['child'].append({'numid': cate.numid, 'title': cate.title, 'url': cate.url})

            all_list.append(dict1)

        # 电影网格列表
        movies = MovieTable.query.all()

        return render_template('movielist.html', cates=all_list, movies=movies,movie_count=len(movies))


class ppp(Resource):
    """
    电影列表
    """

    def get(self):
        return render_template('movielist.html')


class hello(Resource):
    """
    电影列表
    """

    def get(self):
        return render_template('hello.html')
