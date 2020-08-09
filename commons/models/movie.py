from models import db


class CategoryMovie(db.Model):
    """电影列表分类"""
    __tablename__ = 'categroyMovieTable'

    numid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    categroy = db.Column(db.String(100), doc='大分类名称')
    url = db.Column(db.String(100), doc='跳转连接')
    title = db.Column(db.String(100), doc='二级分类名称')
    source = db.Column(db.String(100), doc='分类来源')

    def __repr__(self):
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


class MovieDetailTable(db.Model):
    """电影详情"""
    __tablename__ = 'moviedetailtable'

    id = db.Column(db.Integer, primary_key=True, doc='电影id')
    director = db.Column(db.String(100), doc='导演')
    keyword = db.Column(db.String(500), doc='关键字')
    categroy = db.Column(db.String(500), doc='类别')
    des = db.Column(db.String(3000), doc='描述')
    movie_pers = db.relationship('MoviePerformerTable', primaryjoin='MovieDetailTable.id==MoviePerformerTable.id',
                                 backref='movie_detail')

    def __repr__(self):
        return '<MovieDetailTable %r>' % self.director


class MoviePerformerTable(db.Model):
    """电影里的演员"""
    __tablename__ = 'movieperformertable'

    id = db.Column(db.Integer, db.ForeignKey('moviedetailtable.id'), doc='电影id')
    performer = db.Column(db.String(100), primary_key=True, doc='演员名字')
    role = db.Column(db.String(500), doc='扮演的角色')

    def __repr__(self):
        return '<MoviePerformerTable %r>' % self.performer


class PerformerDetailTable(db.Model):
    """演员详情"""
    __tablename__ = 'performerdetailtable'

    name = db.Column(db.String(100), primary_key=True, unique=True, doc='演员名字')
    e_name = db.Column(db.String(100), doc='演员英文名字')
    alias = db.Column(db.String(200), doc='昵称')
    sex = db.Column(db.String(10), doc='性别')
    bloodtype = db.Column(db.String(5), doc='血型')
    height = db.Column(db.String(10), doc='身高')
    address = db.Column(db.String(500), doc='地址')
    birthday = db.Column(db.String(50), doc='生日')
    constellation = db.Column(db.String(500), doc='星座')
    location = db.Column(db.String(200), doc='本地地址')
    ResidentialAddress = db.Column(db.String(100), doc='详细地址')
    school = db.Column(db.String(100), doc='')
    BrokerageAgency = db.Column(db.String(200), doc='')
    fameyear = db.Column(db.String(200), doc='')
    hobby = db.Column(db.String(1000), doc='')
    Occupation = db.Column(db.String(500), doc='职业')
    weight = db.Column(db.String(200), doc='体重')
    image = db.Column(db.String(1000), doc='头像')
    des = db.Column(db.String(2000), doc='描述')

    def __repr__(self):
        return '<PerformerDetailTable %r>' % self.name
