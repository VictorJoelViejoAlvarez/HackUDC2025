// apiService.js
const API_URL = 'http://localhost:8000'; // URL base de tu API

// Función para obtener personas por nombre
export const getPeopleData = async (nombre) => {
    try {
        const response = await fetch(`${API_URL}/personas?nombre=${nombre}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }

        return await response.json(); // Suponemos que la respuesta es un array de personas
    } catch (error) {
        console.error('Error obteniendo datos de la API:', error);
    }
};
