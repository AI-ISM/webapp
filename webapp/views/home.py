from django.shortcuts import render_to_response
import json


def index(request):
    return render_to_response('home/index.html')
