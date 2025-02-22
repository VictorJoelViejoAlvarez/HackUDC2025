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
    searchButton.addEventListener("click", function (event) {
        event.preventDefault(); // Evitar el envío del formulario
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
});
