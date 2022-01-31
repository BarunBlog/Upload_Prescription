from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Upload_Prescription

from django.db.models.signals import pre_save
from django.dispatch import receiver

import json





@receiver(pre_save, sender=Upload_Prescription)
def Order_Status_Update_Signal(sender, **kwargs):

    the_instance = kwargs['instance']

    if the_instance.id is None:
        pass

    elif the_instance.id:

        previous = Upload_Prescription.objects.get(id=the_instance.id)
        if previous.delivary != the_instance.delivary: # which means delivery field changed

            channel_layer = get_channel_layer()


            async_to_sync(channel_layer.group_send)(
                'id_%s' % the_instance.id, { # group name
                        'type': 'order_status', # custom method name
                        'message': json.dumps('Order status changed'),
                        'delivary': json.dumps(the_instance.delivary)

                    }
                ) 