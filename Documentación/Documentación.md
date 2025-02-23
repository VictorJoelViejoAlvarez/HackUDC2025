# Hack UDC 2025 - Reto de Gradiant - CompetenciApp

Aplicación que permite consultar las competencias de otras personas y consultar si existen soluciones a un problema. Todo con el objetivo de evitar que un problema que ya ha sido resuelto provoque problemas y retrasos.

## Arquitectura del Software

Hemos empleado una arquitectura en 3 capas para desarrollar el frontend y el backend:

1. Interfaz de usuario.
2. Capa de acceso a servicios y capa de servicios.
3. Capa modelo.

## Tecnologías empleadas

### Interfaz de usuario (frontend)

+ HTML5
+ CSS3
+ JavaScrip

### Capa de Acceso a Servicios (frontend)

+ JavaScript

### Capa Servicios (backend)

+ Python
+ FastApi

### Capa Modelo (backend)

+ Python
+ SQLModel

### Base de Datos

+ PostgreSQL

---

La comunicación entre el frontend (cliente) y el backend (servidor) se realiza mediante el uso de una ApiREST desarrollada en python.

---

## Cómo utilizar

El entorno virtual de python ya está preparado.

1. Situarnos en la carpeta raiz del repositorio (HackUDC2025).
2. Activar el entorno virtual de python 3.10 o superior `source .venv/bin/activate`.
3. Arrancar el servidor con `python3 src/backend/main.py`.
4. Abri el repositorio con VsCode.
5. Usando la extensión Live Server de Ritwick Dey para arrancar la aplicación frontend.
6. Probar la aplicación.
