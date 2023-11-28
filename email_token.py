from itsdangerous import URLSafeTimedSerializer


def generate_token(email, app):
    1
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])


def confirm_token(token, app, expiration=3600):
    1
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=expiration
        )
        return email
    except Exception: # localhost:5001/api/confirm/vfvybuibhiutyfuytcyt
        return False
    
