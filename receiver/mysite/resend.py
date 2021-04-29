import json
import thecampy
from os import listdir, environ, remove
from os.path import isfile, join, abspath
from dotenv import load_dotenv

# Enviornment variables
load_dotenv()

ENV = environ

EMAIL = ENV['EMAIL']
PASSWORD = ENV['PASSWORD']

NAME = ENV['NAME']
BIRTH = ENV['BIRTH']
ENTER_DATE = ENV['ENTER_DATE']
UNIT_NAME = ENV['UNIT_NAME']

SUCCESS_DIRECTORY = '/letters/'
FAILED_DIRECTORY = '/letters/failed/'

SOLDIER = thecampy.Soldier(
    NAME, BIRTH, ENTER_DATE, UNIT_NAME
)

client = thecampy.client()


def send_failed_messages():
    print("[*] Retrying failed messages...")

    failed_messages = get_failed_messages()
    for message in failed_messages:
        success = False
        try:
            send_message(message)
            success = True
            print(f"[+] RE-SENT: {message}")
        except:
            print(f"[-] RE-SEND FAILED: {message}")
        finally:
            save_to_file(message, success)


def get_failed_messages():
    message_file_names = [join(FAILED_DIRECTORY, f) for f in listdir(
        FAILED_DIRECTORY) if isfile(join(FAILED_DIRECTORY, f))]

    messages = []
    for message_file_name in message_file_names:
        with open(message_file_name, encoding='utf-8') as f:
            data = json.load(f)
            messages.append(data)

        remove(message_file_name)

    return messages


def send_message(message):
    title = f'({message["sender"]}) {message["title"]}'
    message = thecampy.Message(title, message["content"])

    client.login(EMAIL, PASSWORD)
    client.get_soldier(SOLDIER)
    client.send_message(SOLDIER, message)


def save_to_file(message, success: bool):
    directory = SUCCESS_DIRECTORY if success else FAILED_DIRECTORY
    with open(directory + str(message["id"]) + '.json', 'w', encoding='utf-8') as f:
        json.dump(message, f, ensure_ascii=False)
    return


send_failed_messages()
