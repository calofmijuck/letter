from .models import Message
import thecampy
from .config import NAME, BIRTH, ENTER_DATE, UNIT_NAME, EMAIL, PASSWORD

SOLDIER = thecampy.Soldier(
    NAME, BIRTH, ENTER_DATE, UNIT_NAME
)

client = thecampy.client()


def send_message(message: Message):
    title = f'({message.sender}) {message.title}'
    message = thecampy.Message(title, message.content)

    client.login(EMAIL, PASSWORD)
    client.get_soldier(SOLDIER)
    client.send_message(SOLDIER, message)
