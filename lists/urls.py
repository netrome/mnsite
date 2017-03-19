from django.conf.urls import url

from . import views

app_name = "lists"
urlpatterns = [
    url(r"^$", views.lists_main, name="main"),
    url(r"^items/(?P<list_id>[0-9]+)", views.get_items, name="get_items"),
    url(r"^save/(?P<list_id>[0-9]+)", views.save_items, name="save_items"),
    url(r"^remove/(?P<list_id>[0-9]+)", views.remove_list, name="remove_list"),
    url(r"^share/(?P<list_id>[0-9]+)", views.share_list, name="share_list"),
]
