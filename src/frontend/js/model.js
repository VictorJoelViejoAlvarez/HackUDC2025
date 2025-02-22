const serverIP = "127.0.0.1";
const serverPort = 8000;
const serverUrl = `http://${serverIP}:${serverPort}`;

export async function listarPersonas() {
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

export async function listarPersonasPorNombre(nombre) {
    const url = `${serverUrl}/personas/nombres/${nombre}`;

    // Realizamos la petición a la API
    const response = await fetch(url);
    if (response.ok)
        return await response.json(); // Devolvemos el JSON
    else if (response.status == 404)
        return {}; // Devolvemos un JSON vacío
    else
        throw new Error(`Response status: ${response.status}`); // Lanzamos un error
}

export async function listarCategorias() {
    const url = `${serverUrl}/categorias/`;

    // Realizamos la petición a la API
    const response = await fetch(url);
    if (response.ok)
        return await response.json(); // Devolvemos el JSON
    else if (response.status == 404)
        return {}; // Devolvemos un JSON vacío
    else
        throw new Error(`Response status: ${response.status}`); // Lanzamos un error
}