from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path(
        "scheduled_movies/<int:room_id>/",
        views.RoomSchedulesView.as_view(),
        name="list-movies",
    )
]
