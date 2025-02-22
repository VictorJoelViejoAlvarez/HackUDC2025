const serverIP = "127.0.0.1";
const serverPort = 8000;
const serverUrl = `http://${serverIP}:${serverPort}`;

async function listarPersonas() {
    const url = `${serverUrl}/personas/`;

    // Realizamos la petición a la API
    const response = await fetch(url);
    if (response.ok)
        return await response.json(); // Devolvemos el JSON
    else if (response.status == 404)
        return {}; // Devolvemos un JSON vacío
    else
        throw new Error(`Response status: ${response.status}`); // Lanzamos un error
}