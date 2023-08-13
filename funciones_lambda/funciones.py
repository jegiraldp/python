def maximo(a,b,c):
    return max(a,b,c)

print(maximo(6,15,8))

print("--------------------")

maxim = lambda a,b,c : max(a,b,c)
print(maxim(8,6,12))

print("--------------------")

def ponerPrefijo(prefijo):
    return lambda nombre: f"{prefijo},{nombre}"

addMr = ponerPrefijo("Mr")
addSr = ponerPrefijo("Sr")
addMiss = ponerPrefijo("Miss")

print(addMr("Jorge"))
print(addSr("Eliecer"))
print(addMiss("Maite"))

print("--------------------")

def elevarA(exponente):
    return lambda base : base**exponente

elevarCuadrado=elevarA(2)
elevarCubo=elevarA(3)

print(elevarCuadrado(2))
print(elevarCubo(2))
