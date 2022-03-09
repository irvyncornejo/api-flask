class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG =  True
    SQLALCHEMY_DATABASE_URI = 'postgresql://irvyn:localDB@127.0.0.1:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    DEBUG =  False
    SQLALCHEMY_DATABASE_URI = 'postgresql://irvyn:localDB@127.0.0.1:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'test': TestConfig,
    'development':DevelopmentConfig
}