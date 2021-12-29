import thecampy

from .config import BIRTH, EMAIL, ENTER_DATE, NAME, PASSWORD, UNIT_NAME
from .models import Message

SOLDIER = thecampy.Soldier(NAME, BIRTH, ENTER_DATE, UNIT_NAME)

client = thecampy.Client(EMAIL, PASSWORD)


def format_content(content):
    content = "<p>" + content.replace("\n", "</p><p>") + "</p>"
    content = content.replace("<p></p>", "<p>&nbsp;</p>")
    return content


def send_message(message: Message):
    title = f"({message.sender}) {message.title}"
    message = thecampy.Message(title, format_content(message.content))

    client.get_soldier(SOLDIER)
    client.send_message(SOLDIER, message)
