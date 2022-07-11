from django.http import JsonResponse


def response_data(message: str = '', action:str='', data: dict = {}) -> JsonResponse:
    if action: message=f'{action} success'

    return JsonResponse({
        'status': True,
        'message': message,
        'data': data
    })


def response_error(message: str = '', action:str='', code: int = 400, error_code: int = 400000, error_field: str = 'all', error_message: str = '') -> JsonResponse:
    if action: message=f'{action} fail'
    return JsonResponse({
        'status': False,
        'message': message,
        'errors': {
            'error_code': error_code,
            'error_field': error_field,
            'error_message': error_message
        }
    }, status=code)


METHOD_NOT_ALLOWED = response_error(
    message='method not allowed',
    code=405,
    error_code=405
)
