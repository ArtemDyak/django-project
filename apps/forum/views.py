from django.shortcuts import render, redirect
from django.http import HttpRequest
from . import forms


def index(request: HttpRequest):
    template_kwargs = {
        'user': request.user,
    }
    return render(request, 'forum/index.html', template_kwargs)


def new_message(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {
            'form': forms.MessageForm()
        }

        return render(request, 'forum/new_forum_message.html', template_kwargs)

    # Добавление нового сообщения сделать тут
    return redirect( index )
