from django.shortcuts import render
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json

from chat.models import Message, User, Chat
from chat.forms import CreateNewMessage


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    if request.method == 'GET':
        form = CreateNewMessage()
        messages = Message.objects.filter(chat=Chat.objects.first())
        messages = [message.content for message in messages]
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'messages': messages,
            'form': form
        })
    elif request.method == 'POST':
        content = request.POST.get('mes')
        Message.objects.create(
            chat=Chat.objects.first(),
            user=User.objects.first(),
            content=content
        )
        return JsonResponse({'detail': 'Success!!!'})




