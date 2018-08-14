from . import views
from django.conf.urls import url
from django.contrib import admin
from StreamViewer.settings import production

urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^logout/$', views.user_logout, name='Logout')


]
