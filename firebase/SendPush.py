import FCMmanager as fcm_django

tokens = ["fjzsrkWbN-Q:APA91bFLhG0vAUCehqb9fNmfh980ZGsd9Smnm6oqBDVkvOkm4gCKY8DEKPGpYo4OSVCse45iczEjHg9wbwWp0UbtP0c1puTmpPZRZ9cIrSRzh-vHOu9MoMfPRJYAweLFKD14jgf6-Oc0"]
fcm_django.send_push("Hi", "This is my next", tokens)