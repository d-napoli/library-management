import axios from 'axios';

axios.defaults.xsrfHeaderName = 'x-csrftoken';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.withCredentials = false;
axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Accept'] = 'application/json';
// axios.defaults.headers.common['Access-Control-Allow-Headers'] = "accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-requested-with";
// axios.defaults.headers.common['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"

const httpClient = axios.create({
  baseURL: 'http://0.0.0.0:8000/',
  timeout: 60000,
});

httpClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    return Promise.reject(error);
  },
);

export { httpClient };
