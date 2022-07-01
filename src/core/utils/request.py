import json
from core import logger
from core.utils.response import response_error
from django.http import HttpRequest


def get_data(request: HttpRequest, fields: list or str = []):
    if type(fields) == str:
        fields = [fields]

    value = {}

    for field in fields:
        value[str(field)] = ''

    try:
        json_data = json.loads(request.body)
        for field in fields:
            field = str(field)
            value[field] = json_data.get(field, '')
        return value
    except Exception as e:
        logger.error(str(e))

    try:
        for field in fields:
            field = str(field)
            value[field] = request.POST.get(field, '')
        return value
    except Exception as e:
        logger.error(str(e))
        return value


def required_field(data: dict = {}, fields: list or str = []):
    if type(fields) == str:
        fields = [fields]

    for field in fields:
        if data.get(field, '') == '':
            return response_error(
                message='required fields',
                error_code=400001,
                error_field=field,
                error_message=f'{field} is empty'
            )
