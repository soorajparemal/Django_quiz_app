from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$' , views.main_page,name='main_page'),
    url(r'^result_page' , views.result_page,name='result_page'),
]