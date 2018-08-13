from django.conf.urls import url
from django.contrib import admin
from seinfo import views

urlpatterns = [
    #url(r'^admin/', views.index),
    url(r'^idc_add',views.idc_add, name='idc_add'),
    url(r'^idc_update/(?P<idc_id>[0-9]+)/update/$',views.idc_update, name='idc_update'),
]
