from django.shortcuts import render_to_response
import json


def index(request):
    with open('webapp/jsonApi/mlLists.json', 'r', encoding='utf-8') as f:
        mlAlgoLists = json.load(f)
    with open('webapp/jsonApi/aiLists.json', 'r', encoding='utf-8') as f:
        topLists = json.load(f)

    return render_to_response('ai/ml.html', {'mlAlgoList': mlAlgoLists, 'topList': topLists})
