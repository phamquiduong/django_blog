# Get logger
import logging
logger = logging.getLogger('log')


# Get user model
from django.contrib.auth import get_user_model
User = get_user_model()
