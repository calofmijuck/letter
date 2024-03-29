import json
import sys

from django.shortcuts import render

from .config import DIRECTORY, NAME, RECENT_LETTERS
from .models import Message
from .sender import send_message


def index(request):
    latest_message_list = Message.objects.order_by("-created")[:RECENT_LETTERS]
    response = {"latest_message_list": latest_message_list, "name": NAME}
    return render(request, "letter/index.html", response)


def write(request):
    if request.method == "GET":
        return render(request, "letter/write.html", {})

    data = request.POST
    title, sender, content = data["title"], data["sender"], data["content"]
    content = content.replace("\r", "")

    error = validate_message(title, sender, content)
    if error is not None:
        response = {"title": title, "sender": sender, "content": content, "error": error}
        return render(request, "letter/write.html", response)

    message = Message.create(sender, title, content)
    message.save()

    try:
        send_message(message)
        message.sent = True
        print(f"[+] SENT: {message}", file=sys.stderr)
    except Exception:
        print(f"[-] SEND FAILED: {message}", file=sys.stderr)
    finally:
        message.save()
        save_to_file(message)

    return render(request, "letter/requested.html", {})


def validate_message(title: str, sender: str, content: str) -> str:
    if len(sender) == 0:
        return "작성자를 입력해 주세요."
    elif len(title) == 0:
        return "제목을 입력해 주세요."
    elif len(content) == 0:
        return "내용을 입력해 주세요."
    elif len(content) > 1500:
        return "내용이 너무 깁니다."
    else:
        return None


def save_to_file(message: Message):
    with open(DIRECTORY + str(message.id) + ".json", "w", encoding="utf-8") as f:
        json.dump(message.to_json(), f, ensure_ascii=False)
    return
