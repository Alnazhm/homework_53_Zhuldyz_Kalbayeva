from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def index_view(request: WSGIRequest):
    print(f'Get first {request.GET}')
    first = int(request.GET.get('first', 0))
    second = int(request.GET.get('second', 0))
    return render(request, 'index.html', context={
        'result': first + second,
        'first': first,
        'second': second
    })