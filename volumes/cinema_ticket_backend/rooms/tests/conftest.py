import pytest
from rooms.models import Room

@pytest.fixture
def sample_room():
    return Room.objects.create(
        name="Screen 1",
        seats=100
    )