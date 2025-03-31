import pytest
from django.core.exceptions import ValidationError
from movies.models import Movie

@pytest.mark.django_db
class TestMovieModel:
    def test_movie_creation(self, sample_movie):
        assert sample_movie.title == "Inception"
        assert sample_movie.duration == 148
        assert sample_movie.poster.name.startswith("posters/inception")
        assert str(sample_movie) == "Inception"

    @pytest.mark.django_db
    def test_movie_meta_options(self):
        assert Movie._meta.verbose_name == "Movie"
        assert Movie._meta.verbose_name_plural == "Movies"
        assert Movie._meta.ordering == ["-created"]
        # Updated assertion for created field
        

    def test_title_max_length(self):
        with pytest.raises(ValidationError):
            Movie.objects.create(
                title="A" * 101,
                duration=120,
                poster=None
            ).full_clean()