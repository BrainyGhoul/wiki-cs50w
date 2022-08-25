from django.urls import path

from . import views

app_name = "post_entries"

urlpatterns = [
    path("new_entry", views.index, name="new_entry")
]