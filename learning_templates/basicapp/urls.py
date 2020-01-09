from django.conf.urls import url
from . import views
from django.urls import path
# TEmplate tagging
app_name='basicapp'

urlpatterns=[
    path('relative_url_templates/',views.relative_url_templates,name='relative'),
    path('other/',views.other,name='other'),
]
