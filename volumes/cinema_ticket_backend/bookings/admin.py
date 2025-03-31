from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("schedule", "seat_number", "booked_at")
    list_filter = ("booked_at",)
