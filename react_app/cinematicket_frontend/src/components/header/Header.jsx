import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Modal from 'react-modal';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import api from '../../api';
import './Header.css';

function Header() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [activeTab, setActiveTab] = useState(0);
  const [user, setUser] = useState(null);
  const [formData, setFormData] = useState({
    loginEmail: '',  // Separate fields for login/register
    loginPassword: '',
    registerUsername: '',
    registerEmail: '',
    registerPassword: '',
    registerPassword2: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  // Check auth status on component mount
  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await api.get('users/me/');
        setUser(response.data);
      } catch (err) {
        if (err.response?.status === 401) {
          try {
            const refresh = localStorage.getItem('refresh');
            if (refresh) {
              const refreshResponse = await api.post('users/token/refresh/', { refresh });
              localStorage.setItem('access', refreshResponse.data.access);
              const retryResponse = await api.get('users/me/');
              setUser(retryResponse.data);
            }
          } catch (refreshError) {
            handleLogout();
          }
        }
      }
    };

    if (localStorage.getItem('access')) {
      checkAuth();
    }
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      console.log('here')
      const response = await api.post('users/login/', {
        email: formData.loginEmail,  
        password: formData.loginPassword
      });
      
      localStorage.setItem('access', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
      
      const userResponse = await api.get('users/me/');
      setUser(userResponse.data);
      
      setIsModalOpen(false);
      setError('');
      // Clear only login fields
      setFormData(prev => ({
        ...prev,
        loginEmail: '',
        loginPassword: ''
      }));
    } catch (err) {
      setError(err.response?.data?.detail || 'Invalid email or password');
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    if (formData.registerPassword !== formData.registerPassword2) {
      setError('Passwords do not match');
      return;
    }

    try {
      const response = await api.post('users/register/', {
        username: formData.registerUsername,
        email: formData.registerEmail,
        password: formData.registerPassword,
        password2: formData.registerPassword2
      });

      localStorage.setItem('access', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
      
      const userResponse = await api.get('users/me/');
      setUser(userResponse.data);
      setIsModalOpen(false);
      setError('');
    } catch (err) {
      setError(
        Object.values(err.response?.data || {}).flat()[0] || 
        'Registration failed'
      );
    }
  };

  const handleLogout = async () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setUser(null);
    navigate('/');
  };

  return (
    <header className="cinema-header">
      <div className="header-container">
        <Link to="/" className="logo-link">
          <div className="logo">
            <span className="logo-icon">🎬</span>
            <h1 className="logo-text">CineDemo</h1>
          </div>
        </Link>
        <nav className="main-nav">
          <ul className="nav-list">
            <li className="nav-item">
              <Link to="/" className="nav-link">Home</Link>
            </li>
            <li className="nav-item">
              <Link to="/movies" className="nav-link">Movies</Link>
            </li>
            <li className="nav-item">
              <Link to="/about" className="nav-link">About</Link>
            </li>
          </ul>
        </nav>
        <div className="user-actions">
          {user ? (
            <div className="user-info">
              <span className="username">{user.username}</span>
              <button className="btn btn-logout" onClick={handleLogout}>Logout</button>
            </div>
          ) : (
            <>
              <button className="btn btn-login" onClick={() => {
                setIsModalOpen(true);
                setActiveTab(0);
                setError('');
              }}>Login</button>
              <button className="btn btn-signup" onClick={() => {
                setIsModalOpen(true);
                setActiveTab(1);
                setError('');
              }}>Sign Up</button>
            </>
          )}
        </div>
      </div>

      <Modal
        isOpen={isModalOpen}
        onRequestClose={() => setIsModalOpen(false)}
        className="auth-modal"
        overlayClassName="auth-overlay"
        ariaHideApp={false}
      >
        <Tabs selectedIndex={activeTab} onSelect={index => setActiveTab(index)}>
          <TabList>
            <Tab>Login</Tab>
            <Tab>Register</Tab>
          </TabList>

          <TabPanel>
            <form onSubmit={handleLogin} className="auth-form">
              {error && <div className="error-message">{error}</div>}
              <div className="form-group">
                <label>Email</label>  {/* Changed from Username to Email */}
                <input
                  type="email"
                  name="loginEmail"
                  value={formData.loginEmail}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Password</label>
                <input
                  type="password"
                  name="loginPassword"
                  value={formData.loginPassword}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <button type="submit" className="btn btn-submit">Login</button>
            </form>
          </TabPanel>

          <TabPanel>
            <form onSubmit={handleRegister} className="auth-form">
              {error && <div className="error-message">{error}</div>}
              <div className="form-group">
                <label>Username</label>
                <input
                  type="text"
                  name="registerUsername"
                  value={formData.registerUsername}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  name="registerEmail"
                  value={formData.registerEmail}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Password</label>
                <input
                  type="password"
                  name="registerPassword"
                  value={formData.registerPassword}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Confirm Password</label>
                <input
                  type="password"
                  name="registerPassword2"
                  value={formData.registerPassword2}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <button type="submit" className="btn btn-submit">Register</button>
            </form>
          </TabPanel>
        </Tabs>
      </Modal>
    </header>
  );
}

export default Header;