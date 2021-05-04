import thecampy

from .config import BIRTH, EMAIL, ENTER_DATE, NAME, PASSWORD, UNIT_NAME
from .models import Message

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
