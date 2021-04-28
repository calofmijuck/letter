from .models import Message
from django.shortcuts import render
import json

from typing import Dict

DIRECTORY = '/letters/'

RECENT_LETTERS = 10


def index(request):
    latest_message_list = Message.objects.order_by('-created')[:RECENT_LETTERS] 
    context = {'latest_message_list': latest_message_list}
    return render(request, 'letter/index.html', context)


def write(request):
    if request.method == 'GET':
        return render(request, 'letter/write.html', {})

    data = request.POST
    title, sender, content = data['title'], data['sender'], data['content']

    error = validate_message(title, sender, content)
    if error is not None:
        message_dict = {'title': title, 'sender': sender, 'content': content, 'error': error}
        return render(request, 'letter/write.html', message_dict)

    msg = Message.create(sender, title, content)
    msg.save()

    save_to_file(msg)
    return render(request, 'letter/success.html', {})


def validate_message(title: str, sender: str, content: str) -> str:
    if len(sender) == 0:
        return '작성자를 입력해 주세요.'
    elif len(title) == 0:
        return '제목을 입력해 주세요.'
    elif len(content) == 0:
        return '내용을 입력해 주세요.'
    elif len(content) > 1500:
        return '내용이 너무 깁니다.'
    else:
        return None


def save_to_file(message: Message):
    with open(DIRECTORY + str(message.id) + '.json', 'w', encoding='utf-8') as f:
        json.dump(message.to_json(), f, ensure_ascii=False)
    return
