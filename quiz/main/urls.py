from django.urls import path

from .views import IndexView

app_name = "main"
urlpatterns = [
    path("", view=IndexView.as_view(), name="index"),
]
