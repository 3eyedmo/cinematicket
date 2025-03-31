from django.urls import path
from . import views


app_name = "rooms"
urlpatterns = [
    path("", views.RoomListCreate.as_view(), name="room-list"),  # List and Create rooms
    path(
        "<int:pk>/", views.RoomDetailView.as_view(), name="room-detail"
    ),  # Retrieve, Update, Delete room
]
