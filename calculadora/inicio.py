from suma import suma
from resta import resta
from producto import producto
from division import division

import sys

class inicio:
    
    def inicio():
        inicio.menu()

    
    def menu():
        print("\n-----------------------")
        print("Calculator T2000\n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir\n")
        opcion = input("Digite la opción -> ")
        opcion= int(opcion)
        inicio.proceder(opcion)

        
    
    def proceder(opcion):
        if opcion==5:
            print("\nGracias por utilizar nuestro servicios")
            sys.exit(0)
        else:
            numeroUno = input("Digite número 1 -> ")
            numeroDos = input("Digite número 2 -> ")
            numeroUno = int(numeroUno)
            numeroDos = int(numeroDos)

            if opcion==1:
                print ("Resultado "+ str(suma.calcular(numeroUno,numeroDos)))

            if opcion==2:
                print ("Resultado "+ str(resta.calcular(numeroUno,numeroDos)))
            
            if opcion==3:
                print ("Resultado "+ str(producto.calcular(numeroUno,numeroDos)))
            
            if opcion==4:
                if numeroDos==0:
                    print("\nNo se puede dividir por cero !!!")
                    pass        
                else:
                    print ("Resultado "+ str(division.calcular(numeroUno,numeroDos)))
        inicio.menu()
        
inicio.inicio()