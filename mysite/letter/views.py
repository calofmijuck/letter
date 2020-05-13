from django.http import HttpResponse
from .models import Message
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Message.objects.order_by('-created')[:7]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'letter/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Message, pk=question_id)
    return render(request, 'letter/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# def vote(request):
#     return render(request, 'letter/write.html', {})

def write(request):
    # print(request.method)
    if request.method == "GET":
        return render(request, 'letter/write.html', {})
    
    req = request.POST
    title = req['title']
    sender = req['sender']
    content = req['content']
    message_dict = {'title': title, 'sender': sender, 'content': content}
    if len(sender) == 0:
        message_dict['error'] = "작성자를 입력해 주세요."
    elif len(title) == 0:
        message_dict['error'] = "제목을 입력해 주세요."
    elif len(content) == 0:
        message_dict['error'] = "내용을 입력해 주세요."
    elif len(content) > 1500:
        message_dict['error'] = "내용이 너무 깁니다."

    if 'error' in message_dict:
        return render(request, 'letter/write.html', message_dict)
    else:

        print(sender, title, content)
        return render(request, 'letter/success.html', {})
