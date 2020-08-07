class DefaultConfig(object):
    # DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'LKDSIRMGksdfj345#$@qdhjkh145'
    pass


class ProductionConfig(DefaultConfig):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    FLASK_ENV = 'development'


class TestingConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
