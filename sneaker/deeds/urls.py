from django.conf.urls import url
from deeds import views
urlpatterns = [
 url(r'^$', views.deeds, name='deeds'),
]