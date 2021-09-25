INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (232, 'Gauchondor', 'magia pura', 20, 'Ronaldinhus', '2001-12-12');
INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (9865, 'Parmiterin', 'velocidad', 13, 'Asprillini', '2008-02-28');
INSERT INTO escuela(codigo_escuela, nombre_escuela, habilidad_principal, anios_servicio, creador, fecha_inicio) 
VALUES (22682, 'Riventus', 'precisión', 10, 'Pirlotes', '2011-06-21');

INSERT INTO ingrediente(nombre_ingrediente, peso_promedio, nivel_reaccion, existencia) 
VALUES ('Soda',394,9.3,1);
INSERT INTO ingrediente(nombre_ingrediente, peso_promedio, nivel_reaccion, existencia) 
VALUES ('Borojo',123,8.9,1);
INSERT INTO ingrediente(nombre_ingrediente, nivel_reaccion) 
VALUES ('Tarrito Rojo',0.1);

INSERT INTO pocion(codigo_pocion, nombre_pocion, reg_litros, num_utilizado, codigo_escuela_fk) 
VALUES (12,'Bomba AntiResaca',278.8,400,232);
INSERT INTO pocion(codigo_pocion, nombre_pocion, codigo_escuela_fk) 
VALUES (872,'Borojó con Tarrito Rojo',9865);

INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (12,1,current_time);
INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (872,2,'2019-02-12 18:56:45');
INSERT INTO receta(codigo_pocion_fk,id_ingrediente_fk,fecha_hora_receta)
VALUES (872,3,current_time);