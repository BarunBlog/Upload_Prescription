from django.urls import path
from .consumers import UpdateOrderStatusConsumer


product_ws_patterns = [
    path('orderplaced/order_status/<id>/', UpdateOrderStatusConsumer.as_asgi()),
]