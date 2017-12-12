from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^editor$', views.editor, name='editor'),
    url(r'^note$',  views.content , name="note"),
]