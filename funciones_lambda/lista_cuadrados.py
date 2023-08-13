listaEnteros = [1,2,3,4,5,6,7,8,9]
listaCuadrados=[]

for e in listaEnteros:
    listaCuadrados.append(e ** 2)

print(listaCuadrados)

print("-------------------------------")
listaCuadrados = list(map(lambda g: g ** 2, listaEnteros))
print(listaCuadrados)

print("-------------------------------")
