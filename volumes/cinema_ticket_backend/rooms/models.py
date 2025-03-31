from django.db import models
from helpers.models import TiemstampModel


class Room(TiemstampModel):
    name = models.CharField(max_length=50, unique=True)
    seats = models.PositiveIntegerField(default=80)  # Example: 10 x 8 seats

    class Meta:
        ordering = ["-created"]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        db_table = "rooms"

    def __str__(self):
        return self.name
