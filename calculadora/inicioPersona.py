from persona import persona

p = persona(123,"jorge",2)
print("hola "+p.nombre+" "+str(p.documento))
print ("Hola estático "+str(persona.atributoEstatico))