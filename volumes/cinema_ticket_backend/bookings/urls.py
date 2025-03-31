from django.urls import path
from bookings.views import SeatAvailabilityView, BookSeatView

app_name = "bookings"
urlpatterns = [
    path(
        "seats/<int:schedule_id>/",
        SeatAvailabilityView.as_view(),
        name="available-seats",
    ),
    path("", BookSeatView.as_view(), name="book-seat"),
]
