from producto import producto

p1 = producto(1,'televisor')
p2 = producto(2,'computador')
lista = []
lista.append(p1)
lista.append(p2)

for pro in lista:
    print(f"{pro.codigo} : {pro.nombre}")
    #print(str(pro.codigo)+": "+pro.nombre)