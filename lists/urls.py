from django.conf.urls import url

from . import views

app_name = "lists"
urlpatterns = [
    url(r"^", views.lists_main, name="main"),
]
