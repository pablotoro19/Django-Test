import uuid

from django.conf import settings

from celery import shared_task
from commons.helpers import generate_uuid
from cornershop-test.celery import app
from secret import TOKEN_SLACK
from slackclient import SlackClient

uuid = generate_uuid()
url_menu_today = "http://localhost/menu/%s" % str(uuid)


@shared_task
def send_slack(option):
    token = settings.SLACK_TOKEN
    sc = SlackClient(slack_token)

    options = []
    for o in option:
        options.append(str(o.description))

    option_description = str(options)

    sc.api_call(
        "chat.postMessage",
        channel=settings.SLACK_CHANNEL,
        text="Hola!. \nDejo el menú de hoy :)\n"+ option_description + "\nurl : "+ url_menu_today +" \nTengan un lindo día! "
    )
