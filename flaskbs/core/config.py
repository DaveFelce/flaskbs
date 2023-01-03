"""Flask configuration variables."""
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
env_file = path.join(BASE_DIR, "local.env")
load_dotenv(env_file)


class Config:
    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    DEBUG = False
    TESTING = False

    # Database
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "")
    POSTGRES_DB: str = "flaskbs"
    SQLALCHEMY_DATABASE_URI: str = ""

    @property  # type: ignore [no-redef]
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
