DROP TABLE IF EXISTS Persona;
DROP TABLE IF EXISTS Categoria;
DROP TABLE IF EXISTS Competencia;
DROP TABLE IF EXISTS CompetenciaEmpleado;
DROP TABLE IF EXISTS Problema;
DROP TABLE IF EXISTS Solucion;
DROP TABLE IF EXISTS Autor;

CREATE TABLE Persona (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido1 VARCHAR(30) NOT NULL,
    apellido2 VARCHAR(30) NOT NULL,
    empleado BOOLEAN NOT NULL,
    telefono INTEGER NOT NULL CHECK (telefono >= 0),
    email VARCHAR(50) NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY (id)
);

CREATE TABLE Categoria (
    id BIGINT NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(30) NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY (id)
);

CREATE TABLE Competencia (
    id BIGINT NOT NULL AUTO_INCREMENT,
    competencia VARCHAR(50) NOT NULL,
    categoriaId BIGINT NOT NULL,
    CONSTRAINT pk_id PRIMARY KEY (id),
    CONSTRAINT fk_categoriaId FOREIGN KEY (categoriaId) REFERENCES Categoria(id) ON DELETE CASCADE
);

CREATE TABLE CompetenciaEmpleado(
    empleadoId BIGINT NOT NULL,
    competenciaId BIGINT NOT NULL,
    obtencion VARCHAR(300) NOT NULL,
    CONSTRAINT pk_empleadoId_competenciaId PRIMARY KEY (empleadoId, categoriaId)
    CONSTRAINT fk_empleadoId FOREIGN KEY (empleadoId) REFERENCES Persona(id) ON DELETE CASCADE
    CONSTRAINT fk_competenciaId FOREIGN KEY (competenciaId) REFERENCES Competencia(id) ON DELETE CASCADE
)

CREATE TABLE Problema(

)

CREATE TABLE Solucion(

)

CREATE TABLE Autor(

)