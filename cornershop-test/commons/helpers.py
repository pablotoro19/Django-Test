import uuid


from datetime import datetime

from django.conf import settings
from pytz import timezone


#shared space for common functions

def generate_uuid():
    return uuid.uuid4()

def get_now_cl():
    try:
        tz = timezone('America/Santiago')
        return datetime.now(tz)
    except Exception as e:
        raise Response({'error': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
