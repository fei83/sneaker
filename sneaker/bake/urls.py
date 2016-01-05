from django.conf.urls import url
from bake import views


urlpatterns = [
 url(r'^$', views.bake, name='bake'),
 
 ]