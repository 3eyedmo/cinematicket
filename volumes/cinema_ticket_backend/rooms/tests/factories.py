import factory
from rooms.models import Room

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    name = factory.Sequence(lambda n: f"Screen {n}")
    seats = factory.Faker("random_int", min=50, max=200)