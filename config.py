from os import getenv

class DevConfig:
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': getenv('DB_USER', 'root'),
        'password': getenv('DB_PASSWORD', ''),
        'host': getenv('DB_HOST', 'localhost'),
        'dbname': getenv('DB_NAME')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ECHO = False

Config = DevConfig