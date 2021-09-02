DROP TABLE IF EXISTS receta;
CREATE TABLE receta(
	id_receta int PRIMARY KEY auto_increment,
    codigo_pocion_fk int NULL,
    id_ingrediente_fk int NULL,
    fecha_hora_receta TIMESTAMP,
    FOREIGN KEY(codigo_pocion_fk) REFERENCES pocion(codigo_pocion),
    FOREIGN KEY(id_ingrediente_fk) REFERENCES ingrediente(id_ingrediente)
);
INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (12,1,now());
INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (872,2,'2019-02-12 18:56:45');
INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (872,3,now());