CREATE TABLE receta(
	id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    	codigo_pocion_fk INTEGER NULL,
    	id_ingrediente_fk INTEGER NULL,
    	fecha_hora_receta TIMESTAMP DEFAULT current_timestamp,
    	FOREIGN KEY(codigo_pocion_fk) REFERENCES pocion(codigo_pocion),
    	FOREIGN KEY(id_ingrediente_fk) REFERENCES ingrediente(id_ingrediente)
);