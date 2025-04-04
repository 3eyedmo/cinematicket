from rest_framework import generics

from rooms.serializers import RoomSerializer
from rooms.models import Room


class RoomListApiView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


