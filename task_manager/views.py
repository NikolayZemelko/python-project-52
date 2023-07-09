from django.shortcuts import render


def index(request):

    greeting = 'Hello World!'
    return render(request, 'index.html', context={
        "greeting": greeting,
    })
