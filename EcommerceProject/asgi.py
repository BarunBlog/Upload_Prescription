"""
ASGI config for EcommerceProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from upload_prescription_api.routing import product_ws_patterns



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EcommerceProject.settings')


websocket_patterns = []

websocket_patterns += product_ws_patterns


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(
        websocket_patterns
    ))
})
