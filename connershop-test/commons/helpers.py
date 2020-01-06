import uuid

import slack
from django.conf import settings
from datetime import datetime

from pytz import timezone


def send_slack_notification(uuid):
    """Slack notification."""
    slack_token = settings.SLACK_TOKEN
    sc = SlackClient(slack_token)
    message = "Check the menu of day: " \
              "https://nora.cornershop.io/menu/%s" % uuid
    sc.api_call(
        'chat.postMessage',
        channel=settings.SLACK_CHANNEL,
        text=message
    )

def generate_uuid():
    """Return uuid"""
    return uuid.uuid4().hex

def get_now_cl():
    try:
        tz = timezone('America/Santiago')
        #format = "%Y-%m-%d %H:%M:%S"
        return datetime.now(tz)
    except Exception as e:
        raise Response({'error': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
