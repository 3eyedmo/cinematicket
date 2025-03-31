import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import HomePage from './pages/HomePage';
// import RoomMoviesPage from './pages/RoomMoviesPage';
// import MovieSchedulePage from './pages/MovieSchedulePage';
import Header from './components/header/Header';
import Home from './components/home/Home';
import Movies from './components/movies/Movies';
import Seats from './components/seats/Seats';
function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/rooms/:roomId/movies" element={<Movies />} />
            <Route path="/seats/:scheduleId" element={<Seats />} />
          </Routes>
        </main>
        
      </div>
    </Router>
  );
}

export default App;
