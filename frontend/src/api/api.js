import axios from 'axios';

const BASE_URL = "http://127.0.0.1:5000";

export const registerUser = async (userData) => {
    try {
        const response = await axios.post(`${BASE_URL}/register`, userData);
        return response.data;
    } catch (error) {
        console.error("Registration Error:", error.response.data);
        throw error;
    }
};

export const loginUser = async (userData) => {
    try {
        const response = await axios.post(`${BASE_URL}/login`, userData);
        return response.data;
    } catch (error) {
        console.error("Login Error:", error.response.data);
        throw error;
    }
};
