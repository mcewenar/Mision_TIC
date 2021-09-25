SELECT 'Consulta 1';
SELECT * FROM escuela;
SELECT 'Consulta 2';
SELECT pocion.codigo_pocion, pocion.nombre_pocion,printf("%.2f", pocion.reg_litros) , pocion.num_utilizado, escuela.nombre_escuela, escuela.habilidad_principal FROM pocion JOIN escuela 
ON pocion.codigo_escuela_fk = escuela.codigo_escuela; 
SELECT 'Consulta 3';
SELECT ingrediente.nombre_ingrediente, ingrediente.existencia, ingrediente.nivel_reaccion, pocion.nombre_pocion 
FROM ingrediente 
JOIN receta ON ingrediente.id_ingrediente = receta.id_ingrediente_fk 
JOIN pocion ON pocion.codigo_pocion = receta.codigo_pocion_fk 
WHERE receta.codigo_pocion_fk=872
ORDER BY ingrediente.nombre_ingrediente;