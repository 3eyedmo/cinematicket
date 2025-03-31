from django.utils import timezone

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from movies.models import Movie, Schedule
from rooms.models import Room
from movies.serializers import MovieSerializer, ScheduleSerializer


class ListMovieAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        room_id = self.kwargs.get("room_id")
        now = timezone.now()
        return Movie.objects.filter(
            schedule__room_id=room_id, schedule__start_time__gt=now
        ).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": "No movies scheduled for this room."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RoomSchedulesView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        room_id = self.kwargs["room_id"]
        return Schedule.objects.filter(room_id=room_id).select_related("movie")

    def list(self, request, *args, **kwargs):
        try:
            room_id = kwargs["room_id"]
            # Verify room exists
            Room.objects.get(pk=room_id)
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({"success": True, "data": serializer.data})
        except Room.DoesNotExist:
            return Response(
                {"success": False, "message": "Room not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CreateMovieAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
