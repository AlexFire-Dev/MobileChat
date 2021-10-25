from django.conf import settings


def info(request):
    DEBUG = settings.DEBUG

    if DEBUG:
        HTTP_PROTOCOL = 'http'
        WEBSOCKET_PROTOCOL = 'ws'
    else:
        HTTP_PROTOCOL = 'https'
        WEBSOCKET_PROTOCOL = 'wss'

    return {
        'debug': DEBUG,
        'address': settings.ADDRESS,
        'http_protocol': HTTP_PROTOCOL,
        'websocket_protocol': WEBSOCKET_PROTOCOL,
        'google_client_id': settings.GOOGLE_CLIENT_ID,
    }
