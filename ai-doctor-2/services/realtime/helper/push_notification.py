import firebase_admin
from firebase_admin import messaging, credentials

# Load Firebase credentials
cred = credentials.Certificate("path/to/firebase-credentials.json")
firebase_admin.initialize_app(cred)

def send_push_notification(token: str, title: str, body: str):
    """
    Sends a push notification to a mobile device using Firebase Cloud Messaging (FCM).
    """
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token,
    )
    response = messaging.send(message)
    return response

