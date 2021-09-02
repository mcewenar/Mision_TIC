DELETE FROM escuela where codigo_escuela = 22682;
UPDATE pocion SET reg_litros=1240.2,num_utilizado=2334 WHERE codigo_pocion=872;
UPDATE receta SET fecha_hora_receta=now() WHERE id_receta=3;
UPDATE ingrediente SET nivel_reaccion=4.1,existencia=false WHERE id_ingrediente=3;
