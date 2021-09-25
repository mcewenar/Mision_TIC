CREATE TABLE ingrediente(
	id_ingrediente INTEGER PRIMARY KEY AUTOINCREMENT,
    	nombre_ingrediente varchar(30) NOT NULL,
    	peso_promedio INTEGER default 0,
    	nivel_reaccion decimal(10,1) NOT NULL,
    	existencia INTEGER default 0
);