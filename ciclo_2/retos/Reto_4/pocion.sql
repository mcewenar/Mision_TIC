DROP TABLE IF EXISTS pocion;
CREATE TABLE pocion(
	codigo_pocion int NOT NULL PRIMARY KEY,
	nombre_pocion varchar(30) NOT NULL,
    reg_litros decimal(6,2) default 0, 
    num_utilizado int NULL,
    codigo_escuela_fk int NOT NULL,
    FOREIGN KEY(codigo_escuela_fk) REFERENCES escuela(codigo_escuela)
);
INSERT INTO pocion(codigo_pocion, nombre_pocion, reg_litros, num_utilizado, codigo_escuela_fk) 
VALUES (12,'Bomba AntiResaca',278.8,400,232);
INSERT INTO pocion(codigo_pocion, nombre_pocion, codigo_escuela_fk) 
VALUES (872,'Borojo con Tarrito Rojo',9865);