from django.conf.urls import url
from . import views

appname = 'resizer1'

urlpatterns = [
    url(r'^$', views.EArticleView.as_view(), name='article'),
]
