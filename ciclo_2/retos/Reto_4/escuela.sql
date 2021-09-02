DROP TABLE IF EXISTS escuela;
CREATE TABLE escuela(
	codigo_escuela int NOT NULL PRIMARY KEY,
    nombre_escuela varchar(40) NOT NULL,
    habilidad_principal varchar(40) NOT NULL,
    anios_servicio int NOT NULL,
    creador varchar(20) NOT NULL,
    fecha_inicio date
);
INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (232, 'Gauchondor', 'magia pura', 20, 'Ronaldinhus', '2001-12-12');
INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (9865, 'Parmiterin', 'velocidad', 13, 'Asprillini', '2008-02-28');
INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (22682, 'Riventus', 'precisión', 10, 'Pirlotes', '2011-06-21');