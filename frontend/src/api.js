import axios from 'axios'

const api = axios.create ({
    baseURL: "https://nba-prop-generator.onrender.com",
    headers: {
    'Content-Type': 'application/json',
  },
});

export default api;