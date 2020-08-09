from flask import render_template
from flask_restful import Resource, reqparse
from sqlalchemy import text

from models import db_session
from models.movie import CategoryMovie, MovieTable


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
        rp = reqparse.RequestParser()
        rp.add_argument('page', type=int, location=['args'], default=1)
        rp.add_argument('pagesize', type=int, location=['args'], default=30)
        params = rp.parse_args()
        pagesize = params.pagesize
        offset = (params.page - 1) * pagesize
        # movies = MovieTable.query.order_by(MovieTable.score.desc()).offset(offset).limit(pagesize).all()
        movies = MovieTable.query.offset(offset).limit(pagesize).all()
        total = len(MovieTable.query.all())
        if total % pagesize == 0:
            total_page = total / pagesize
        else:
            total_page = total / pagesize + 1
        return render_template('movielist.html', cates=all_list, movies=movies, total=total, page_num=params.page,
                               total_page=int(total_page))


class MoviePlay(Resource):
    def get(self):
        rp = reqparse.RequestParser()
        rp.add_argument('movieid', location='args', default=858)
        rp.add_argument('playhtml', location='args')
        params = rp.parse_args()
        movie_id = params.movieid

        # movie_id = 858

        stmt = text(
            "SELECT md.id,mt.moviename,mt.score,md.director,md.categroy,md.keyword,md.des,group_concat(mp.performer) AS perman,group_concat(mp.role) AS role \
        FROM movietable AS mt INNER JOIN (moviedetailtable AS md,movieperformertable AS mp) ON \
        mt.id = md.id AND mt.id = mp.id AND md.id = mp.id \
        WHERE md.id =:x GROUP BY md.id")

        groups = db_session.execute(stmt, params={'x': movie_id}).first()

        pers = groups[7].split(sep=',')
        roles = groups[8].split(sep=',')
        per_role = []
        for i in range(len(pers)):
            per_role.append({'per': pers[i], 'role': roles[i]})

        movie_detail = {'movieid': groups[0], 'moviename': groups[1], 'score': groups[2], 'director': groups[3],
                        'categroy': groups[4], 'keyword': groups[5], 'des': groups[6], 'per_role': per_role}

        # return movie_detail
        return render_template('movieplay.html', movie_detail=movie_detail)


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
