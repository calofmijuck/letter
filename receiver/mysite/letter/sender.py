from .models import Message
from dotenv import load_dotenv
import thecampy
import os

load_dotenv()

ENV = os.environ

EMAIL = ENV['EMAIL']
PASSWORD = ENV['PASSWORD']

NAME = ENV['NAME']
BIRTH = ENV['BIRTH']
ENTER_DATE = ENV['ENTER_DATE']
UNIT_NAME = ENV['UNIT_NAME']


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
