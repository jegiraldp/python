from persona import persona

class inicio:
    def iniciar():
        doc = int(input("Digite documento -> "))
        nombre = input("Digite Nombre -> ")
        edad = int(input("Digite edad -> "))
        
        p = persona(doc,nombre,edad)

        print("Persona registrada\n"+
              str(p.documento) +"--"+p.nombre+":"+str(p.edad))

inicio.iniciar()