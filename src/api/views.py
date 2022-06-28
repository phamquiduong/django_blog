from core.utils.request import get_data, required_field
from core.utils.login import login_by_username


def login(request):
    data = get_data(request=request, fields=['username', 'password'])
    required = required_field(data=data, fields=['username', 'password'])
    if required is not None: return required
    return login_by_username(username=data['username'], password=data['password'])
