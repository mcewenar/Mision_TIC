DROP TABLE IF EXISTS ingrediente;
CREATE TABLE ingrediente(
	id_ingrediente int PRIMARY KEY auto_increment,
    nombre_ingrediente varchar(30) NOT NULL,
    peso_promedio int default 0,
    nivel_reaccion decimal(10,1) NOT NULL,
    existencia boolean default false
);
INSERT INTO ingrediente(nombre_ingrediente, peso_promedio, nivel_reaccion, existencia) 
VALUES ('Soda',394,9.3,true);
INSERT INTO ingrediente(nombre_ingrediente, peso_promedio, nivel_reaccion, existencia) 
VALUES ('Borojo',123,8.9,true);
INSERT INTO ingrediente(nombre_ingrediente, nivel_reaccion) 
VALUES ('Tarrito Rojo',0.1);