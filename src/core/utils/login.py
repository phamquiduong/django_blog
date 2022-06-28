from django.contrib.auth import authenticate
from core.utils.response import response_data, response_error
from core.helper.jwt_helper import jwt_encode
import datetime


ACCESS_TOKEN_TIME = datetime.timedelta(hours=1)
REFRESH_TOKEN_TIME = datetime.timedelta(days=30)


def login_by_username(username: str, password: str):
    user = authenticate(username=username, password=password)

    if user:
        ACCESS_PAYLOAD = {
            'user_id': user.id,
            'exp': datetime.datetime.now() + ACCESS_TOKEN_TIME
        }

        REFRESH_PAYLOAD = {
            'user_id': user.id,
            'exp': datetime.datetime.now() + REFRESH_TOKEN_TIME
        }

        return response_data(
            message='login success',
            data={
                'access_token': jwt_encode(ACCESS_PAYLOAD),
                'refresh_token': jwt_encode(REFRESH_PAYLOAD)
            }
        )
    else:
        return response_error(
            message='login fail',
            code=403,
            error_code=403001,
            error_message='username or password incorrect'
        )
