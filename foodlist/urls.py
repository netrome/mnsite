from django.conf.urls import url

from . import views

app_name = "foodlist"
urlpatterns = [
    url(r'^$', views.main_view, name='main'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]
