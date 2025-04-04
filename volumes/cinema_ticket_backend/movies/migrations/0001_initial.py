# Generated by Django 5.1.7 on 2025-03-26 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "poster",
                    models.ImageField(upload_to="posters/", verbose_name="Poster"),
                ),
                (
                    "duration",
                    models.IntegerField(
                        help_text="Duration in minutes", verbose_name="Duration"
                    ),
                ),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
                "db_table": "movies",
                "ordering": ["-created"],
                "indexes": [
                    models.Index(fields=["created"], name="movies_created_b626af_idx"),
                    models.Index(fields=["title"], name="movies_title_179e04_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("start_time", models.DateTimeField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="rooms.room",
                    ),
                ),
            ],
            options={
                "verbose_name": "Schedule",
                "verbose_name_plural": "Schedules",
                "ordering": ["start_time"],
            },
        ),
    ]
