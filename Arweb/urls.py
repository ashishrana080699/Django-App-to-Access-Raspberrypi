from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('/on', views.on, name='on'),
    path('/off', views.off, name='off'),
    path('/camera', views.off, name='camera'),
]
