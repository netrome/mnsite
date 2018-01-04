from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('get_value/', views.get_value, name="get_value"),
]