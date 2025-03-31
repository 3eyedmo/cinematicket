import pytest
from django.utils import timezone
from movies.models import Movie, Schedule
from rooms.models import Room
from bookings.models import Booking
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def sample_user():
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def sample_movie():
    return Movie.objects.create(
        title="The Matrix",
        duration=136,
        poster=None
    )

@pytest.fixture
def sample_room():
    return Room.objects.create(
        name="Screen 1",
        seats=100
    )

@pytest.fixture
def sample_schedule(sample_movie, sample_room):
    return Schedule.objects.create(
        movie=sample_movie,
        room=sample_room,
        start_time=timezone.now() + timezone.timedelta(days=1)
    )

@pytest.fixture
def sample_booking(sample_user, sample_schedule):
    return Booking.objects.create(
        schedule=sample_schedule,
        user=sample_user,
        seat_number="A1",
        booked_at=timezone.now()
    )