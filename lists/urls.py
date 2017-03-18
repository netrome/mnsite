from django.conf.urls import url

from . import views

app_name = "lists"
urlpatterns = [
    url(r"^$", views.lists_main, name="main"),
    url(r"^items/(?P<list_id>[0-9]+)", views.get_items, name="get_items"),
]
