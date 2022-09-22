import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(
    "/Users/user/Downloads/django-rest-framework-crud-master/firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def send_push(title, msg, registration_token, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg),
        data=dataObject,
        tokens=registration_token,
    )

    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
