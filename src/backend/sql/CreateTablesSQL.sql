DROP TABLE IF EXISTS Persona cascade;
DROP TABLE IF EXISTS Categoria cascade;
DROP TABLE IF EXISTS Competencia cascade;
DROP TABLE IF EXISTS CompetenciaEmpleado cascade;
DROP TABLE IF EXISTS Problema cascade;
DROP TABLE IF EXISTS Solucion cascade;
DROP TABLE IF EXISTS Autor cascade;

CREATE TABLE Persona (
    id BIGSERIAL NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    apellido1 VARCHAR(30) NOT NULL,
    apellido2 VARCHAR(30) NOT NULL,
    empleado BOOLEAN NOT null DEFAULT TRUE,
    telefono VARCHAR(9) NOT NULL,
    email VARCHAR(50) NOT NULL,
    CONSTRAINT pk_idPersona PRIMARY KEY (id)
);

CREATE TABLE Categoria (
    id BIGSERIAL NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    CONSTRAINT pk_idCategoria PRIMARY KEY (id)
);

CREATE TABLE Competencia (
    id BIGSERIAL NOT NULL,
    competencia VARCHAR(50) NOT NULL,
    categoriaId BIGSERIAL NOT NULL,
    CONSTRAINT pk_idCompetencia PRIMARY KEY (id),
    CONSTRAINT fk_CompetenciaCategoriaId_CategoriaId FOREIGN KEY (categoriaId) REFERENCES Categoria(id) ON DELETE CASCADE
);

CREATE TABLE CompetenciaEmpleado(
    empleadoId BIGSERIAL NOT NULL,
    competenciaId BIGSERIAL NOT NULL,
    obtencion TEXT NOT NULL,
    verificado BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT pk_empleadoId_competenciaId PRIMARY KEY (empleadoId, competenciaId),
    CONSTRAINT fk_CompetenciaEmpleadoEmpleadoId_PersonaId FOREIGN KEY (empleadoId) REFERENCES Persona(id) ON DELETE cascade,
    CONSTRAINT fk_CompetenciaEmpleadoCompetenciaId_CompetenciaId FOREIGN KEY (competenciaId) REFERENCES Competencia(id) ON DELETE CASCADE
);

CREATE TABLE Problema(
    id BIGSERIAL NOT NULL,
    problema TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    competenciaId BIGSERIAL NOT NULL,
    CONSTRAINT pk_idProblema PRIMARY KEY (id),
    CONSTRAINT fk_ProblemaCompetenciaId_CompetenciaId FOREIGN KEY (competenciaId) REFERENCES Competencia(id) ON DELETE CASCADE
);

CREATE TABLE Solucion(
    id BIGSERIAL NOT NULL,
    problemaId BIGSERIAL NOT NULL,
    fecha TIMESTAMP NOT NULL,
    rutaDocumentacion TEXT NOT NULL,
    CONSTRAINT pk_idSolucion PRIMARY KEY (id),
    CONSTRAINT fk_SolucionProblemaId_ProblemaId FOREIGN KEY (problemaId) REFERENCES Problema(id) ON DELETE CASCADE
);

CREATE TABLE Autor(
    personaId BIGSERIAL NOT NULL,
    solucionId BIGSERIAL NOT NULL,
    CONSTRAINT fk_AutorPersonaId_PersonaId FOREIGN KEY (personaId) REFERENCES Persona(id) ON DELETE CASCADE,
    CONSTRAINT fk_AutorSolucionId_SolucionId FOREIGN KEY (solucionId) REFERENCES Solucion(id) ON DELETE CASCADE
);