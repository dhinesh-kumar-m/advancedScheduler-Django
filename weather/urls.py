from django.urls import re_path
from weather import views


urlpatterns = [
    re_path(r'^$', views.MainPage.as_view())
]