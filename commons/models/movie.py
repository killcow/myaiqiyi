from models import db


class CategoryMovie(db.Model):
    """电影列表分类"""
    __tablename__ = 'categroyMovieTable'

    numid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    categroy = db.Column(db.String(100), doc='大分类名称')
    url = db.Column(db.String(100), doc='跳转连接')
    title = db.Column(db.String(100), doc='二级分类名称')
    source = db.Column(db.String(100), doc='分类来源')

    def __repr____(self):
        return '<CategoryMovie %s %s>' % (self.categroy, self.title)


class MovieTable(db.Model):
    """电影列表list"""
    __tablename__ = 'movietable'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    moviename = db.Column(db.String(100), doc='电影名称')
    time = db.Column(db.String(100), doc='电影播放长度')
    url = db.Column(db.String(100), doc='电影地址')
    imagepath = db.Column(db.String(2000), doc='图片地址')
    saveimagepath = db.Column(db.String(500), doc='图片本地保存地址')
    score = db.Column(db.Float, doc='评分')
    status = db.Column(db.Integer, doc='状态')
    source = db.Column(db.String(10), doc='来源')

    def __repr__(self):
        return '<MovieTable %r>' % self.moviename
