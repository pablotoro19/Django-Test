import uuid


from datetime import datetime

from django.conf import settings
from pytz import timezone




def generate_uuid():
    return uuid.uuid4()

def get_now_cl():
    try:
        tz = timezone('America/Santiago')
        #format = "%Y-%m-%d %H:%M:%S"
        return datetime.now(tz)
    except Exception as e:
        raise Response({'error': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
