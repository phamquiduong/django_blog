import os
from functools import wraps

from django.http import HttpRequest

from core import User
from core.helper.jwt_helper import jwt_decode
from core.utils.response import response_error

AUTH_HEADER = os.getenv('AUTH_HEADER', 'www-authenticate')


def required_login(view):
    @wraps(view)
    def view_func(request: HttpRequest, *args, **kwargs):
        token = request.headers.get(AUTH_HEADER, '')

        decode = jwt_decode(token=token)

        if 'errors' in decode:
            return response_error(
                message='auth fail',
                code=403,
                error_code=403002,
                error_field=AUTH_HEADER,
                error_message=decode['errors']
            )

        try:
            user_id = decode.get('payload', {}).get('user_id', 0)
            user = User.objects.get(id=user_id)
            kwargs.update({
                'user': user
            })
            return view(request, *args, **kwargs)
        except Exception as e:
            return response_error(
                message='auth fail',
                code=403,
                error_code=403002,
                error_field=AUTH_HEADER,
                error_message=str(e)
            )

    return view_func
