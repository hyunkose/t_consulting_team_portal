import datetime
import uuid
import jwt


def get_token(username = "shko", client_id = "26196bdf-ed61-482e-bc6c-069b30235afa", secret_id = "79179fae-25ee-4e27-85fe-48828f462d7f", secret_value = "uJz9+Sy4YMMbXcj+qlVYwXePOMvWZ6V1r44k3P51od4="):

    token = jwt.encode(
        {
            "iss": client_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": username,
            "scp": ["tableau:views:*", "tableau:content:*"]
        },
            secret_value,
            algorithm = "HS256",
            headers = {
            'kid': secret_id,
            'iss': client_id
            }
    )

    return token