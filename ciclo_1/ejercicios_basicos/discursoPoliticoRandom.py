import random
lambetazo = ["Queridos","Apreciados","Distinguidos","Honorables","Estimados","Respetados"]
potenciales_Marranos = ["compatriotas","conciudadanos","hijitos","copartidarios","ciudadanías libres","electores"]
condicion = ["en mi gobierno","con su apoyo","siendo elegido","con su ayuda","si me siguen","durante mi mandato"]
compromiso = ["voy a derrotar","venceré","eliminaré","acabaré","lucharé contra","combatiré"]
ilusion_guerrerista = ["La violencia y","la delincuencia y","la corrupción y","la inflación y","la pobreza y","el desplazamiento y"]
promesa = ["trabajaré por", "garantizaré","protegeré","velaré por","promoveré","defenderé"]
beneficio_populista = ["la educación","el empleo","la seguridad","la paz","la igualdad","la salud"]
dependiendo_de_votos = ["del país", "de la ciudad", "de la comunidad", "de la población","para toda la gente", "de cada colombiano"]

choice_lambetazo = random.choice(lambetazo) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
choice_potencialesMarranos = random.choice(potenciales_Marranos)
choice_condicion = random.choice(condicion)
choice_compromiso = random.choice(compromiso)
choice_ilusion = random.choice(ilusion_guerrerista)
choice_promesa = random.choice(promesa)
choice_beneficio_populista = random.choice(beneficio_populista)
choice_dependiendoVotos = random.choice(dependiendo_de_votos)

print("Discurso político generado: ", choice_lambetazo, choice_potencialesMarranos,",", choice_condicion, choice_compromiso, choice_ilusion, choice_promesa, choice_beneficio_populista, choice_dependiendoVotos)
print("Discurso político generado: ", choice_lambetazo +" "+ choice_potencialesMarranos +", "+ choice_condicion +" "+ choice_compromiso +" "+ choice_ilusion +" "+ choice_promesa +" "+ choice_beneficio_populista +" "+ choice_dependiendoVotos)