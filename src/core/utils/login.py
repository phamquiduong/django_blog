from django.contrib.auth import authenticate
from core.utils.response import response_data, response_error
from core.helper.jwt_helper import jwt_encode, jwt_decode
import datetime


ACCESS_TOKEN_TIME = datetime.timedelta(hours=1)
ACCESS_TOKEN_TYPE = 'ACCESS'

REFRESH_TOKEN_TIME = datetime.timedelta(days=180)
REFRESH_TOKEN_TYPE = 'REFRESH'


def login_by_username(username: str, password: str):
    user = authenticate(username=username, password=password)

    if user:
        ACCESS_PAYLOAD = {
            'user_id': user.id,
            'type': ACCESS_TOKEN_TYPE,
            'exp': datetime.datetime.now() + ACCESS_TOKEN_TIME
        }

        REFRESH_PAYLOAD = {
            'user_id': user.id,
            'type': REFRESH_TOKEN_TYPE,
            'exp': datetime.datetime.now() + REFRESH_TOKEN_TIME
        }

        return response_data(
            action='login',
            data={
                'access_token': jwt_encode(ACCESS_PAYLOAD),
                'refresh_token': jwt_encode(REFRESH_PAYLOAD)
            }
        )
    else:
        return response_error(
            action='login',
            code=403,
            error_code=403001,
            error_message='username or password incorrect'
        )


def get_token(refresh_token:str):
    decode = jwt_decode(token=refresh_token)
    if 'payload' in decode:
        user_id = decode['payload'].get('user_id', 0)
        ACCESS_PAYLOAD = {
            'user_id': user_id,
            'exp': datetime.datetime.now() + ACCESS_TOKEN_TIME
        }

        REFRESH_PAYLOAD = {
            'user_id': user_id,
            'exp': datetime.datetime.now() + REFRESH_TOKEN_TIME
        }

        return response_data(
            action='get token',
            data={
                'access_token': jwt_encode(ACCESS_PAYLOAD),
                'refresh_token': jwt_encode(REFRESH_PAYLOAD)
            }
        )
    else:
        return response_error(
            action='get token',
            error_code=400002,
            error_field='refresh_token',
            error_message=decode.get('errors')
        )
