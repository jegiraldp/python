from suma import suma
import sys

class inicioCalculadora:

    def menu():
        print ("Calculator T2000")
        print ("1. Sumar")
        print ("2. Restar")
        print ("5. Salir")
        opcion = int(input("Digite opción -> "))
        inicioCalculadora.proceder(opcion)

    def proceder(opcion):
        if opcion==5:
            print("Gracias por utilizar nuestros servicios")
            sys.exit(0)

        else:
            numeroUno = input("Digite número 1 -> ")
            numeroDos = input("Digite número 2 -> ")
            numeroUno = int(numeroUno)
            numeroDos = int(numeroDos)

        if(opcion==1):
            print("El resultado es "+str(suma.calcular(numeroUno,numeroDos)))
            inicioCalculadora.menu()


inicioCalculadora.menu()
        
        