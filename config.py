from dotenv import dotenv_values
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv_vals =  dotenv_values(".env")

class Config(object):
    SECURITY_PASSWORD_SALT = dotenv_vals["SECURITY_PASSWORD_SALT"]
    SECRET_KEY = dotenv_vals["SECRET_KEY"]
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = dotenv_vals["EMAIL_USER"]
    MAIL_PASSWORD = dotenv_vals["EMAIL_PASSWORD"]
    
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()