import * as model from './model.js';

document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById("data");
    const formFields = document.getElementById("form2");
    const tableSelector = document.getElementById("tableselector");
    const searchButton = document.querySelector(".searchbutton");
    const nameInput = document.getElementById("nombrePersona");

    // Ocultar la tabla al inicio
    table.style.display = "none";
    formFields.style.display = "none";

    // Mostrar tabla cuando se presiona el botón buscar
    searchButton.addEventListener("click", async function (event) {
        const tablePersona = document.getElementById("table-1");

        event.preventDefault(); // Evitar el envío del formulario

        const nombre = nameInput.value.trim();

        data;
        if (!nombre) {
            data = await model.listarPersonas();
        }
        else {
            data = await model.listarPersonasPorNombre(nombre);
        }

        const tableBody = document.querySelector("#table-1 tbody");

        tableBody.innerHTML = "";
        // Llenar la tabla con los resultados
        if (data && data.length > 0) {
            data.forEach(persona => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${persona.id}</td>
                    <td>${persona.nombre}</td>
                    <td>${persona.apellido1}</td>
                    <td>${persona.apellido2}</td>
                    <td>${persona.empleado ? 'Sí' : 'No'}</td>
                    <td>${persona.telefono}</td>
                    <td>${persona.email}</td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            const row = document.createElement('tr');
            row.innerHTML = `<td colspan="7">No se encontraron resultados</td>`;
            tableBody.appendChild(row);
        }

        // Mostrar la tabla
        table.style.display = "block";
    });

    // Mostrar campos solo si se selecciona "Personas"
    tableSelector.addEventListener("change", function () {
        if (tableSelector.value === "1") {
            formFields.style.display = "block";
        } else {
            formFields.style.display = "none";
        }
    });

    // Obtener el valor del nombre cuando se necesite
    function getNombre() {
        return nameInput.value;
    }

    // Exponer la función para obtener el nombre si es necesario
    window.getNombre = getNombre;

    function showDisplay(item) {
        item.style.display = 'block';
    }

    function hideDisplay(item) {
        item.style.display = 'none';
    }
});