"""Flask configuration variables."""
import os

from os import path
from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


class Settings(BaseSettings):
    # General Config
    SECRET_KEY: str = ""
    FLASK_APP: str = "flaskbs"
    DEBUG: bool = False
    TESTING: bool = False

    # Database
    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = "flaskbs"
    SQLALCHEMY_DATABASE_URI: str = ""

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    @classmethod
    def assemble_db_connection(cls, v: str, values: dict[str, Any]) -> Any:
        if v != "":
            db_uri = v.format(values["POSTGRES_DB"])
        else:
            db_uri = PostgresDsn.build(
                scheme="postgresql",
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_HOST"),
                port=values.get("POSTGRES_PORT"),
                path="/" + values.get("POSTGRES_DB", ""),
            )

        return db_uri

    class Config:
        case_sensitive = True
        # env var settings priority ie priority 1 will override priority 2:
        # 1 - env vars read from *local.env file
        # 2 - values assigned directly in the Settings class
        env_file = os.path.join(BASE_DIR, "local.env")
        env_file_encoding = "utf-8"


class DevelopmentSettings(Settings):
    DEVELOPMENT: bool = True
    DEBUG: bool = True


class TestingSettings(Settings):
    TESTING: bool = True
    DEBUG: bool = True
    POSTGRES_DB: str = "flaskbs_test"


settings = Settings()
development_settings = DevelopmentSettings()
testing_settings = TestingSettings()
