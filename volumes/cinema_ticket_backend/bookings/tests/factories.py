import factory
from django.utils import timezone
from bookings.models import Booking
from movies.tests.factories import MovieFactory, ScheduleFactory
from rooms.tests.factories import RoomFactory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    user = factory.SubFactory(UserFactory)
    schedule = factory.SubFactory(ScheduleFactory)
    seat_number = factory.Sequence(lambda n: f"A{n}")
    booked_at = factory.LazyFunction(timezone.now)