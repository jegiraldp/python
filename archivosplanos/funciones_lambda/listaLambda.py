lista=[1,2,3,4,5,6,7,9]
impares=[]

for num in lista:
    if num%2!=0:
        impares.append(num)

print(impares)
print("------------------------")

losImpares = [x for x in lista if x%2!=0]
print(losImpares)

print("------------------------")
los_impares = filter(lambda x: x%2 !=0, lista)
print(list(los_impares))

