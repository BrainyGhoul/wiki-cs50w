from django.urls import path

from . import views


app_name = "goto_entries"

urlpatterns = [
    path("<str:entry>", views.index, name="show_entry"),
    path("", views.redirect, name="redirect")
]