class DefaultConfig(object):
    SECRET_KEY = 'LKDSIRMGksdfj345#$@qdhjkh145'
    # flask-sqlalchemy使用的参数
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/MovieSpider'
    # SQLALCHEMY_BINDS = {
    #     'bj-m1': 'mysql://root:mysql@127.0.0.1:3306/toutiao',
    #     'bj-s1': 'mysql://root:mysql@127.0.0.1:8306/toutiao',
    #     'masters': ['bj-m1'],
    #     'slaves': ['bj-s1'],
    #     'default': 'bj-m1'
    # }

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = True



class ProductionConfig(DefaultConfig):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    # FLASK_ENV = 'development'


class TestingConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
