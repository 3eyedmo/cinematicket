from django.utils import timezone

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from movies.models import Schedule
from rooms.models import Room
from movies.serializers import ScheduleSerializer



class RoomSchedulesView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        room_id = self.kwargs["room_id"]
        now = timezone.now()
        return Schedule.objects.filter(room_id=room_id, start_time__gt=now).select_related("movie")

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


