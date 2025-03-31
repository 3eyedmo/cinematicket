from rest_framework.serializers import ModelSerializer
from movies.models import Movie, Schedule


class MovieSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Movie


class ScheduleSerializer(ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ["id", "movie", "start_time", "created", "updated"]
        read_only_fields = ["created", "updated"]
