import axios from 'axios';

export default axios.create({
  method: 'GET'
  , baseURL: 'http://localhost:3000'
  , headers: {
    'Access-Control-Allow-Origin': '*'
    , 'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
  }
  , withCredentials: true
})