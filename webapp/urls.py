"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import home, article, ai, knows, user

home_patterns = ([
    path('', home.index, name='index'),
    path('edit/', article.edit, name='edit'),
], 'home')

article_patterns = ([
    path('', article.index, name='index'),
    path('<int:articleId>/', article.article, name='article'),
], 'article')

ai_ml_patterns = ([
    path('', ai.ml.index),
    path('svm/', ai.ml.svm),
    path('knn/', ai.ml.knn),
], 'machineLearning')

ai_dp_patterns = ([
    path('', ai.dp.index),
], 'deepLearning')

ai_dm_patterns = ([
    path('', ai.dp.index),
], 'dateMining')

ai_npl_patterns = ([
    path('', ai.npl.index),
], 'NPL')

ai_patterns = ([
    path('', ai.index),
    path('ml/', include(ai_ml_patterns)),
    path('dp/', include(ai_dp_patterns)),
    path('dm/', include(ai_dm_patterns)),
    path('npl/', include(ai_npl_patterns))
], 'ai')

knows_patterns = ([
    path('', knows.index, name='index'),
], 'knows')

user_patterns = ([
    path('', user.index, name='index'),
], 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_patterns)),
    path('article/', include(article_patterns)),
    path('article/', include(article_patterns)),
    path('ai/', include(ai_patterns)),
    path('knows/', include(knows_patterns)),
    path('user/', include(user_patterns)),
]

