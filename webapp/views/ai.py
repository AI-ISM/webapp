from django.shortcuts import render_to_response
import json
import webapp.views.machineLearning as ml
import webapp.views.deepLearning as dp
import webapp.views.dataMining as dm
import webapp.views.NPL as npl


def index(request):
    with open('webapp/jsonApi/mlLists.json', 'r', encoding='utf-8') as f:
        mlAlgoLists = json.load(f)
    with open('webapp/jsonApi/aiLists.json', 'r', encoding='utf-8') as f:
        topLists = json.load(f)
    with open('webapp/jsonApi/aiArticleLists.json', 'r', encoding='utf-8') as f:
        aiArticleLists = json.load(f)

    return render_to_response('ai/ai.html', {'mlAlgoList': mlAlgoLists, 'topList': topLists, 'aiArticleList': aiArticleLists})

