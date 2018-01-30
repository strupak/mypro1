from django.conf.urls import url
from resizer import views

app_name='resizer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
]