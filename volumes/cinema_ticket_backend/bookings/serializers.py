# serializers.py
from rest_framework import serializers
from movies.models import Movie, Schedule
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Booking
from django.utils import timezone


User = get_user_model()


class BookingSchema(serializers.Serializer):
    schedule = serializers.IntegerField()
    seat_number = serializers.CharField()

class MovieSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "poster", "duration"]

    def get_poster(self, obj):
        request = self.context.get("request")
        if obj.poster:
            return (
                request.build_absolute_uri(obj.poster.url)
                if request
                else obj.poster.url
            )
        return None


class ScheduleSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Schedule
        fields = ["id", "movie", "room", "start_time"]


class SeatSerializer(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.IntegerField()
    is_booked = serializers.BooleanField()
    is_booked_by_you = serializers.BooleanField()


class SeatAvailabilitySerializer(serializers.Serializer):
    movie = MovieSerializer()
    schedule = ScheduleSerializer()
    seats = SeatSerializer(many=True)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["schedule", "seat_number"]
        extra_kwargs = {
            "schedule": {"write_only": True},
            "seat_number": {"write_only": True},
        }

    def validate_seat_number(self, value):
        """Validate seat format like A1, B2, etc."""
        if len(value) < 2 or not value[0].isalpha() or not value[1:].isdigit():
            raise ValidationError(
                "Invalid seat format. Expected format like 'A1', 'B2', etc."
            )
        return value

    def validate(self, data):
        """Validate the booking as a whole"""
        schedule = data["schedule"]
        seat_number = data["seat_number"]
        user = self.context["request"].user

        # Check if seat is already booked
        if Booking.objects.filter(schedule=schedule, seat_number=seat_number).exists():
            raise ValidationError({"seat_number": "This seat is already booked"})

        return data

    def create(self, validated_data):
        """Create the booking"""
        booking = Booking(
            schedule=validated_data["schedule"],
            user=self.context["request"].user,
            seat_number=validated_data["seat_number"],
            booked_at=timezone.now(),
        )
        booking.save()
        return booking
