from django.db import models
from movies.models import Schedule
from django.conf import settings


class Booking(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = ("schedule", "seat_number")  # Prevents double booking

    def __str__(self):
        return f"Booking for seat {self.seat_number} by {self.user.username}"
