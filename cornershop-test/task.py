import uuid

from django.conf import settings

from celery import shared_task
from commons.helpers import generate_uuid
from cornershop-test.celery import app
from secret import TOKEN_SLACK
from slackclient import SlackClient

uuid = generate_uuid()
url_menu = "http://localhost/menu/%s" % str(uuid)


@shared_task
def send_slack(options):
    token = settings.SLACK_TOKEN
    sc = SlackClient(slack_token)

    menu_options = []
    for o in option:
        menu_options.append(str(o.description))

    descriptions = str(menu_options)

    sc.api_call(
        "chat.postMessage",
        channel=settings.SLACK_CHANNEL,
        text="Hola!. \nDejo el menú de hoy :)\n"+ descriptions + "\nurl : "+ url_menu +" \nTengan un lindo día! "
    )
