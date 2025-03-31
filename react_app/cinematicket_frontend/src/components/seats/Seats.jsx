import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Seats.css';
import api from '../../api';
import Modal from 'react-modal';
import Loading from '../helpers/Loading';

Modal.setAppElement('#root');

const Seats = () => {
    const { scheduleId } = useParams();
    const [isUserLoggedIn, setIsUserLoggedIn] = useState(null);
    const [seats, setSeats] = useState([]);
    const [movie, setMovie] = useState(null);
    const [schedule, setSchedule] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedSeat, setSelectedSeat] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [bookingSuccess, setBookingSuccess] = useState(false);

    const checkAuth = () => {
        const refreshToken = localStorage.getItem('refresh');
        if (!refreshToken) {
            setIsUserLoggedIn(false);
        } else {
            setIsUserLoggedIn(true);
        }
    }
    useEffect(() => {
        checkAuth();
        const fetchSeatData = async () => {
            try {
                const response = await api.get(`book/seats/${scheduleId}/`);
                setMovie(response.data.data.movie);
                setSchedule(response.data.data.schedule);
                setSeats(response.data.data.seats);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchSeatData();
    }, [scheduleId]);

    const handleSeatClick = (seat) => {
        if (!seat.is_booked) {
            checkAuth();
            setSelectedSeat(seat);
            setIsModalOpen(true);
        }
    };

    const handleBookSeat = async () => {
        try {
            
            await api.post(
                'book/',
                {
                    schedule: scheduleId,
                    seat_number: selectedSeat.name
                }
            );

            setBookingSuccess(true);
            setIsModalOpen(false);

            // Refresh seat data
            const response = await api.get(
                `book/seats/${scheduleId}/`
            );
            setSeats(response.data.data.seats);
        } catch (err) {
            setError(err.response?.data?.error || 'Failed to book seat');
            setIsModalOpen(false);
        }
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setBookingSuccess(false);
    };

    if (loading) {
        return <Loading></Loading>;
    }

    if (error) {
        return <div className="error">Error: {error}</div>;
    }

    return (
        <div className="seat-booking-container">
            {movie && schedule && (
                <div className="movie-info">
                    <img src={movie.poster} alt={movie.title} className="movie-poster" />
                    <div className="movie-details">
                        <h1>{movie.title}</h1>
                        <p>Duration: {Math.floor(movie.duration / 60)}h {movie.duration % 60}m</p>
                        <p>Showtime: {new Date(schedule.start_time).toLocaleString()}</p>
                    </div>
                </div>
            )}

            <div className="screen">SCREEN</div>

            <div className="seat-map">
                {seats.map((seat) => (
                    <div
                        key={`${seat.name}-${seat.number}`}
                        className={`seat ${seat.is_booked ? 'booked' : ''} ${seat.is_booked_by_you ? 'your-booking' : ''}`}
                        onClick={() => handleSeatClick(seat)}
                    >
                        {seat.name}
                    </div>
                ))}
            </div>

            <div className="seat-legend">
                <div className="legend-item">
                    <div className="legend-color available"></div>
                    <span>Available</span>
                </div>
                <div className="legend-item">
                    <div className="legend-color booked"></div>
                    <span>Booked</span>
                </div>
                <div className="legend-item">
                    <div className="legend-color your-booking"></div>
                    <span>Your Booking</span>
                </div>
            </div>

            <Modal
                isOpen={isModalOpen}
                onRequestClose={closeModal}
                className="booking-modal"
                overlayClassName="booking-overlay"
            >
                {
                    <>
                        <h2>Confirm Booking</h2>
                        {!isUserLoggedIn ? (
                            <div className="login-prompt">
                                <p>Login From Header Of Page</p>
                                <button
                                    onClick={() => closeModal()}
                                    className="login-button"
                                >
                                    Close
                                </button>
                            </div>
                        ) : (
                            <>
                                <p>You're about to book seat <strong>{selectedSeat?.name}</strong></p>
                                <div className="modal-buttons">
                                    <button onClick={closeModal} className="cancel-button">Cancel</button>
                                    <button onClick={handleBookSeat} className="confirm-button">Confirm</button>
                                </div>
                            </>
                        )}
                    </>
                }
            </Modal>
        </div>
    );
};

export default Seats;