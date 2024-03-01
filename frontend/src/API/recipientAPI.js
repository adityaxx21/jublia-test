import axios from "axios";

const BASE_URL = `${process.env.REACT_APP_BASE_URL}/recipient`; // Your API base URL


export const recipientAPI = async (resource, data = null, path=null) => {
  try {
    var response
    switch (resource) {
      case "GET":
        response = await axios.get(BASE_URL);
        break;
      case "POST":
        response = await axios.post(BASE_URL, data);
        break; // Return the data from the response
      case "PUT":
        response = await axios.put(`${BASE_URL}/${path}`, data);
        break;
      case "DELETE":
        response = await axios.delete(`${BASE_URL}/${path}`);
        break;
      default:
        throw new Error(`Invalid method: ${resource}`);
    }
    return response.data; // Return the data from the response
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error; // Rethrow the error to handle it in the component
  }
};
