CREATE TABLE usuario(
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    rool BOOLEAN NOT NULL,
    correo_electronico VARCHAR(50) NOT NULL,
    contraseña VARCHAR(20) NOT NULL
);

CREATE TABLE sintoma(
    id_sintoma INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(50)
);

CREATE TABLE signo(
    id_signo INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(50)
);

CREATE TABLE enfermedad(
    id_enfermedad INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(50)
);

CREATE TABLE enfermedad_sintoma(
    id_enfermedad INT,
    id_sintoma INT,
    PRIMARY KEY (id_enfermedad, id_sintoma),
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedad(id_enfermedad),
    FOREIGN KEY (id_sintoma) REFERENCES sintoma(id_sintoma)
);

CREATE TABLE enfermedad_signo(
    id_enfermedad INT,
    id_signo INT,
    PRIMARY KEY (id_enfermedad, id_signo),
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedad(id_enfermedad),
    FOREIGN KEY (id_signo) REFERENCES signo(id_signo)
);

CREATE TABLE prueba(
    id_prueba INT PRIMARY KEY,
    tipo_prueba BOOLEAN NOT NULL,
    fecha_prueba DATE,
    resultado VARCHAR(50)
);

CREATE TABLE diagnostico(
    id_diagnostico INT PRIMARY KEY,
    id_usuario INT,
    id_prueba INT,
    fecha_diagnostico DATE,
    resultado VARCHAR(50),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_prueba) REFERENCES prueba(id_prueba)
);

CREATE TABLE paciente(
    id_paciente INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE,
    sexo BOOLEAN,
    telefono VARCHAR(10)
);

CREATE TABLE historial(
    id_paciente INT,
    id_diagnostico INT,
    PRIMARY KEY (id_paciente, id_diagnostico),
    FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente),
    FOREIGN KEY (id_diagnostico) REFERENCES diagnostico(id_diagnostico)
);