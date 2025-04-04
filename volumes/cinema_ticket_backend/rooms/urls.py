from django.urls import path
from . import views


app_name = "rooms"
urlpatterns = [
    path("", views.RoomListApiView.as_view(), name="room-list"),  # List rooms
]
