from django.http import JsonResponse


def response_data(message: str = '', data: dict = {}) -> JsonResponse:
    return JsonResponse({
        'status': True,
        'message': message,
        'data': data
    })


def response_error(message: str = '', code: int = 400, error_code: int = 400000, error_field: str = 'all', error_message: str = '') -> JsonResponse:
    return JsonResponse({
        'status': False,
        'message': message,
        'errors': {
            'error_code': error_code,
            'error_field': error_field,
            'error_message': error_message
        }
    }, status=code)
