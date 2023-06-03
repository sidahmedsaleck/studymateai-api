import os 
import dotenv
dotenv.load_dotenv()


class BaseConfig:
    DEBUG=False
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]


class DevelopmentConfig(BaseConfig):
    DEBUG=True


class TestingConfig(BaseConfig):
    TESTING=True
    DEBUG=True

class ProductionConfig(BaseConfig):
    pass


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = BaseConfig.SECRET_KEY




