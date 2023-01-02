"""Flask configuration variables."""
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
env_file = path.join(BASE_DIR, "local.env")
load_dotenv(env_file)


class Config:
    TESTING = False
    DB_SERVER = "localhost"
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    DEBUG = False

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    DEBUG = True
