import time

def saludar(nombre):
    return ("Hola mundo "+nombre)

def hora():
    hora=time.strftime("%H:%M:%S")
    return hora

#print (saludar("Jorge") + " -- La hora es: "+hora())