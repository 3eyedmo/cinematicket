from rest_framework import generics

from rooms.serializers import RoomSerializer
from rooms.models import Room


class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
