from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message

class MyModel(FCMDevice):
    def subscribing(self):
        FCMDevice.objects.all().handle_topic_subscription(True, topic="TOPIC NAME")
        device = FCMDevice.objects.all().first()
        device.handle_topic_subscription(True, topic="TOPIC NAME")


    def finnaly(self):
        message = Message(topic="A topic")
        FCMDevice.objects.send_message(message)

    def unsubscribing(self):
        FCMDevice.objects.all().handle_topic_subscription(False, topic="TOPIC NAME")
        device = FCMDevice.objects.all().first()
        device.handle_topic_subscription(False, topic="TOPIC NAME")