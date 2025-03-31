import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import IntegrityError
from bookings.models import Booking

@pytest.mark.django_db
class TestBookingModel:
    def test_booking_creation(self, sample_booking):
        assert sample_booking.seat_number == "A1"
        assert str(sample_booking) == "Booking for seat A1 by testuser"
        assert sample_booking.user.username == "testuser"
        assert sample_booking.schedule.movie.title == "The Matrix"

    def test_booking_meta_options(self):
        assert Booking._meta.verbose_name == "Booking"
        assert Booking._meta.verbose_name_plural == "Bookings"
        assert Booking._meta.unique_together == (('schedule', 'seat_number'),)

    def test_seat_number_max_length(self, sample_schedule, sample_user):
        with pytest.raises(ValidationError):
            booking = Booking.objects.create(
                schedule=sample_schedule,
                user=sample_user,
                seat_number="A1234567890",  # Too long
                booked_at=timezone.now()
            )
            booking.full_clean()

    def test_unique_together_constraint(self, sample_booking):
        with pytest.raises((ValidationError, IntegrityError)):
            Booking.objects.create(
                schedule=sample_booking.schedule,
                user=sample_booking.user,
                seat_number=sample_booking.seat_number,
                booked_at=timezone.now()
            ).full_clean()

    def test_booking_timestamps(self, sample_booking):
        assert sample_booking.booked_at is not None
        assert sample_booking.booked_at <= timezone.now()