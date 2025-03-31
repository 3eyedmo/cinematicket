import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Home.css';
import Loading from '../helpers/Loading';
import getApiDomain from '../../endpoints';

const Home = () => {
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRooms = async () => {
      try {
        const response = await axios.get(getApiDomain() + '/api/rooms/');
        setRooms(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchRooms();
  }, []);

  const handleRoomClick = (roomId) => {
    navigate(`/rooms/${roomId}/movies`);
  };

  if (loading) {
    return <Loading></Loading>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="home-container">
      <h1 className="home-header">Available Rooms</h1>
      <div className="rooms-grid">
        {rooms.map((room) => (
          <div 
            key={room.id} 
            className="room-card"
            onClick={() => handleRoomClick(room.id)}
          >
            <div className="room-name">{room.name}</div>
            <div className="room-details">
              <div className="room-seats">
                <span className="detail-label">Seats:</span>
                <span className="detail-value">{room.seats}</span>
              </div>
              <div className="room-schedules">
                <span className="detail-label">Schedules:</span>
                <span className="detail-value">{room.number_of_schedules}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;