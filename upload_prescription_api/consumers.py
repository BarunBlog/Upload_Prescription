
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json


class UpdateOrderStatusConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["id"]
        self.room_group_name = 'id_%s' % self.room_name

        # Adding room_name and group_name to the channel
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept() # accept the request from frontend

        self.send(text_data=json.dumps({'status': "Websocket Connected"})) # send data to frontend


    
    def disconnect(self, *args, **kwargs):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        self.send(text_data=json.dumps({'status': "Websocket disconnected"}))

    
    def order_status(self, event):
        
        order = json.loads(event['message'])
        status = json.loads(event['delivary'])
        
        self.send(text_data=json.dumps({
            'Payload': order,
            'delivary': status
        }))