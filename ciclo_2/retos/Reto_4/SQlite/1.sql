CREATE TABLE escuela(
	codigo_escuela int NOT NULL PRIMARY KEY,
    	nombre_escuela varchar(40) NOT NULL,
    	habilidad_principal varchar(40) NOT NULL,
    	anios_servicio int NOT NULL,
    	creador varchar(20) NOT NULL,
    	fecha_inicio date
);