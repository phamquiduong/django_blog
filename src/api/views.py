from core.utils.request import get_data, required_field
from core.utils.response import METHOD_NOT_ALLOWED
from core.utils.login import login_by_username, get_token
from core.decorator.authentication import required_login
from core.utils.response import response_data

from main.models import Menu


def login(request):
    if request.method == 'POST':
        data = get_data(request=request, fields=['username', 'password'])
        required = required_field(data=data, fields=['username', 'password'])
        if required is not None:
            return required
        return login_by_username(username=data['username'], password=data['password'])
    else:
        return METHOD_NOT_ALLOWED


def token(request):
    if request.method == 'POST':
        data = get_data(request=request, fields='refresh_token')
        required = required_field(data=data, fields='refresh_token')
        if required is not None:
            return required
        return get_token(refresh_token=data['refresh_token'])
    else:
        return METHOD_NOT_ALLOWED


@required_login('GET')
def user(request, *args, **kwargs):
    if request.method == 'GET':
        user = kwargs['user']
        return response_data(
            action='get user info',
            data={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
        )
    else:
        return METHOD_NOT_ALLOWED


@required_login(['POST'])
def menu(request, *args, **kwargs):
    if request.method == 'GET':
        display = request.GET.get('display', 'list')
        if display.lower() == 'tree':
            return response_data(
                action='get menu',
                data={'menus': Menu.get_tree()}
            )
        else:
            return response_data(
                action='get menu',
                data={'menus': Menu.get_list()}
            )
    else:
        return METHOD_NOT_ALLOWED
