from .models import Message
from .sender import send_message


def send_failed_messages():
    print("[*] Retrying failed messages...")

    failed_messages = Message.objects.filter(sent=False)
    for message in failed_messages:
        try:
            send_message(message)
            message.sent = True
            message.save()
        except:
            print(f"[-] RE-SEND FAILED: {message}")
