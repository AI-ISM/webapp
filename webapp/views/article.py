from django.shortcuts import render_to_response
import json


def index(request):
    with open('webapp/jsonApi/aiArticleLists.json', 'r', encoding='utf-8') as f:
        aiArticleLists = json.load(f)

    return render_to_response('article/index.html', {'aiArticleList': aiArticleLists})


def article(request, articleId):

    return render_to_response('article/article.html', {'id':articleId})


def edit(request):
    return render_to_response('article/edit.html')