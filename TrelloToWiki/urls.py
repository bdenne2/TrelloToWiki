from django.conf.urls import patterns, url

from TrelloToWiki import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
