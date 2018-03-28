from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


def news(request):
    return render_to_response('news.html')


def ml(request):
    return render_to_response('ml.html')
