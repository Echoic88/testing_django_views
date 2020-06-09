from django.urls import path
from .views import index

app_name = "views_tests_app"
urlpatterns = [
    path("", index, name="index"),
]
