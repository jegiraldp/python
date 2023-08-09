from producto import producto

p1 = producto(1,'televisor')
p2 = producto(2,'computador')
p3 = producto(3,'mesa')
lista = []
lista.append(p1)
lista.append(p2)
lista.append(p3)
#lista.insert(2,p3)
#lista.remove(p1)
#lista.pop(1)
print(lista.count(p1))
lista.reverse()
print(len(lista))


for pro in lista:
    print(f"{pro.codigo} : {pro.nombre}")
    #print(str(pro.codigo)+": "+pro.nombre)