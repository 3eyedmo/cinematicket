import factory
from django.utils import timezone
from movies.models import Movie, Schedule
from rooms.models import Room

class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker("sentence", nb_words=3)
    duration = factory.Faker("random_int", min=60, max=180)
    poster = factory.django.ImageField(color="blue")

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room
    
    name = factory.Faker("word")
    seats = factory.Faker("random_int", min=50, max=200)

class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule

    movie = factory.SubFactory(MovieFactory)
    room = factory.SubFactory(RoomFactory)
    start_time = factory.LazyFunction(lambda: timezone.now() + timezone.timedelta(days=1))