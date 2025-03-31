from django.contrib import admin
from movies.models import Movie, Schedule


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "poster", "duration")
    search_fields = ("title",)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "room", "start_time")
    list_filter = ("room", "start_time")
    search_fields = ("movie__title", "room__name")
    ordering = ("start_time",)
