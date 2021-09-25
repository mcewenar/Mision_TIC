CREATE TABLE pocion(
	codigo_pocion INTEGER NOT NULL PRIMARY KEY,
	nombre_pocion varchar(30) NOT NULL,
    	reg_litros decimal(6,2) default 0, 
    	num_utilizado INTEGER NULL,
    	codigo_escuela_fk INTEGER NOT NULL,
    	FOREIGN KEY(codigo_escuela_fk) REFERENCES escuela(codigo_escuela)
);