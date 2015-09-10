from django.conf.urls import url
from HITtopic import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),
    url(r'^create_topic/$',views.create_topic),
    url(r'^detail/(\d+)/$',views.detail),
    url(r'^mytopic/$',views.mytopic_index),

    ]
