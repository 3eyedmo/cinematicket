import os
import pytest
import django
from django.core.files.uploadedfile import SimpleUploadedFile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema_ticket.settings")
django.setup()

from movies.models import Movie, Schedule  
from rooms.models import Room

@pytest.fixture
def sample_movie():
    return Movie.objects.create(
        title="Inception",
        duration=148,
        poster=SimpleUploadedFile("inception.jpg", b"file_content", content_type="image/jpeg")
    )

@pytest.fixture
def sample_room():
    return Room.objects.create(name="Screen 1", seats=100)

@pytest.fixture
def sample_schedule(sample_movie, sample_room):
    from django.utils import timezone
    return Schedule.objects.create(
        movie=sample_movie,
        room=sample_room,
        start_time=timezone.now() + timezone.timedelta(days=1)
    )