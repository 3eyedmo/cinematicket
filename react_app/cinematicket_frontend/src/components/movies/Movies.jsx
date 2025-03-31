import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import './Movies.css';
import Loading from '../helpers/Loading';
import getApiDomain from '../../endpoints';

const Movies = () => {
  const { roomId } = useParams();
  const navigate = useNavigate();
  const [scheduledMovies, setScheduledMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchScheduledMovies = async () => {
      try {
        const response = await axios.get(`${getApiDomain()}/api/scheduled_movies/${roomId}/`);
        if (response.data.success) {
          setScheduledMovies(response.data.data);
        } else {
          setError('Failed to fetch scheduled movies');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchScheduledMovies();
  }, [roomId]);

  const formatDateTime = (dateTimeString) => {
    const options = { 
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    };
    return new Date(dateTimeString).toLocaleDateString('en-US', options);
  };

  const formatDuration = (minutes) => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}m`;
  };

  const handleBookNow = (scheduleId) => {
    navigate(`/seats/${scheduleId}`);
  };

  if (loading) {
    return <Loading></Loading>
  }

  if (error) {
    return <div className="error-container">Error: {error}</div>;
  }

  if (scheduledMovies.length === 0) {
    return <div className="no-movies">No movies scheduled for this room</div>;
  }

  return (
    <div className="movies-container">
      <h1 className="movies-header">Scheduled Movies</h1>
      <div className="movies-grid">
        {scheduledMovies.map((schedule) => (
          <div key={schedule.id} className="movie-card">
            <div className="movie-poster-container">
              <img 
                src={schedule.movie.poster} 
                alt={schedule.movie.title} 
                className="movie-poster"
                onError={(e) => {
                  e.target.onerror = null;
                  e.target.src = 'https://via.placeholder.com/300x450?text=No+Poster';
                }}
              />
            </div>
            <div className="movie-details">
              <h2 className="movie-title">{schedule.movie.title}</h2>
              <div className="movie-info">
                <div className="info-item">
                  <span className="info-label">Duration:</span>
                  <span>{formatDuration(schedule.movie.duration)}</span>
                </div>
                <div className="info-item">
                  <span className="info-label">Showtime:</span>
                  <span>{formatDateTime(schedule.start_time)}</span>
                </div>
              </div>
              <button 
                className="book-button"
                onClick={() => handleBookNow(schedule.id)}
              >
                Book Now
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Movies;