from datetime import datetime

from .models import Message
from .sender import send_message


def send_failed_messages():
    failed_messages = Message.objects.filter(sent=False)
    if len(failed_messages) == 0:
        return

    print(f"[*] Retrying {len(failed_messages)} failed messages...")
    for message in failed_messages:
        try:
            send_message(message)
            message.sent = True
            message.save()
            print(f"[+] RE-SENT: {message}")
        except:
            print(f"[-] RE-SEND FAILED: {message}")


def test():
    print(f"Cron is working! {datetime.now()}")
