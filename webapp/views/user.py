from django.shortcuts import render_to_response
import json


def index(request):
    html = "welcome"

    return render_to_response(html)
