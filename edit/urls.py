from django.urls import path
from . import views

app_name = "Edit"

urlpatterns = [
    path("<str:entry>", views.index, name="edit_entry")
]