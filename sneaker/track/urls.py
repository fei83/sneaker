from django.conf.urls import url
from track import views
urlpatterns = [
 url(r'^$', views.track, name='track'),
]