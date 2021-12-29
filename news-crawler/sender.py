from datetime import datetime

import thecampy
from config import BIRTH, EMAIL, ENTER_DATE, NAME, PASSWORD, UNIT_NAME

SOLDIER = thecampy.Soldier(NAME, BIRTH, ENTER_DATE, UNIT_NAME)


def send(subject, content):
    content += "\n[FINISH]"
    msg_num = 0
    char_count, enter_count = 0, 0
    buffer = []
    for i, char in enumerate(content):
        buffer.append(char)
        char_count += 1
        if char == "\n":
            enter_count += 1

        if char_count > 1495 or enter_count > 22 or i == len(content) - 1:
            _send(subject + f" - {msg_num}", "".join(buffer))

            char_count, enter_count = 0, 0
            buffer = []

            msg_num += 1


def format_content(content):
    content = "<p>" + content.replace("\n", "</p><p>") + "</p>"
    content = content.replace("<p></p>", "<p>&nbsp;</p>")
    return content


def _send(subject, content):
    try:
        formatted_content = format_content(content)
        message = thecampy.Message(subject, formatted_content)
        
        client = thecampy.Client(EMAIL, PASSWORD)
        client.get_soldier(SOLDIER)
        client.send_message(SOLDIER, message)
        print(f"[+] {datetime.now()} - NEWS SENT")
    except Exception:
        print(f"[-] {datetime.now()} - SEND FAILED")
