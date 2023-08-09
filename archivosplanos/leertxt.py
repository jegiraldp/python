with open('C:\\codeall\\python\\archivosplanos\\archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)


with open('C:\\codeall\\python\\archivosplanos\\archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea, end='')


with open('C:\\codeall\\python\\archivosplanos\\archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print(linea, end='')

