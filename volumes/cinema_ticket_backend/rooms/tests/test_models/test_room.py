import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rooms.models import Room

@pytest.mark.django_db
class TestRoomModel:
    def test_room_creation(self, sample_room):
        assert sample_room.name == "Screen 1"
        assert sample_room.seats == 100
        assert str(sample_room) == "Screen 1"

    def test_room_meta_options(self):
        assert Room._meta.verbose_name == "Room"
        assert Room._meta.verbose_name_plural == "Rooms"
        assert Room._meta.ordering == ["-created"]
        assert Room._meta.db_table == "rooms"

    def test_name_uniqueness(self, sample_room):
        with pytest.raises((ValidationError, IntegrityError)):
            Room.objects.create(
                name=sample_room.name,  # Duplicate name
                seats=80
            ).full_clean()

    def test_seats_positive_integer(self):
        with pytest.raises((ValidationError, IntegrityError)):
            room = Room.objects.create(
                name="Invalid Screen",
                seats=-10  # Negative seats
            )
            room.full_clean()

    def test_name_max_length(self):
        with pytest.raises(ValidationError):
            room = Room.objects.create(
                name="A" * 51,  # Exceeds max_length=50
                seats=80
            )
            room.full_clean()

    def test_default_seats(self):
        room = Room.objects.create(name="Default Screen")
        assert room.seats == 80  # Default value