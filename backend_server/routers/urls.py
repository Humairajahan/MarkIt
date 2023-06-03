from django.urls import path
from . import views

urlpatterns = [
    path("checkIn", views.CheckIn.as_view())
]
