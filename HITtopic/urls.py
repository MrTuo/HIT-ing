from django.conf.urls import url
from HITtopic import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    
    ]
