// userService.js
import axios from 'axios';

const BASE_URL = process.env.REACT_APP_BASE_URL;; // Your API base URL

export const getEmails = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/get_emails`);
    return response.data; // Return the data from the response
  } catch (error) {
    console.error('Error fetching users:', error);
    throw error; // Rethrow the error to handle it in the component
  }
};
