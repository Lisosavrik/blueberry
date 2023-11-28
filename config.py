from dotenv import dotenv_values

dotenv_vals =  dotenv_values(".env")

class Config(object):
    SECURITY_PASSWORD_SALT = dotenv_vals["SECURITY_PASSWORD_SALT"]
    SECRET_KEY = dotenv_vals["SECRET_KEY"]
    MAIL_DEFAULT_SENDER = "noreply@flask.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = dotenv_vals["EMAIL_USER"]
    MAIL_PASSWORD = dotenv_vals["EMAIL_PASSWORD"]
