from django.db import models
from helpers.models import TiemstampModel
from rooms.models import Room


class Movie(TiemstampModel):
    title = models.CharField(verbose_name="Title", max_length=100)
    poster = models.ImageField(verbose_name="Poster", upload_to="posters/")
    duration = models.IntegerField(
        verbose_name="Duration", help_text="Duration in minutes"
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "movies"

        indexes = [
            models.Index(fields=["created"]),
            models.Index(fields=["title"]),
        ]

    def __str__(self):
        return self.title


class Schedule(TiemstampModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="schedules")
    start_time = models.DateTimeField()

    class Meta:
        ordering = ["start_time"]
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return f"{self.movie.title} in {self.room.name} at {self.start_time}"
