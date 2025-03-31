import pytest
from movies.models import Schedule

@pytest.mark.django_db
class TestScheduleModel:
    def test_schedule_creation(self, sample_schedule):
        assert str(sample_schedule) == f"Inception in Screen 1 at {sample_schedule.start_time}"
        assert sample_schedule.movie.title == "Inception"
        assert sample_schedule.room.name == "Screen 1"

    def test_schedule_meta_options(self):
        assert Schedule._meta.verbose_name == "Schedule"
        assert Schedule._meta.verbose_name_plural == "Schedules"
        assert Schedule._meta.ordering == ["start_time"]

    def test_foreign_key_relations(self, sample_schedule):
        assert sample_schedule.movie.schedule_set.count() >= 1
        assert sample_schedule.room.schedules.count() >= 1
