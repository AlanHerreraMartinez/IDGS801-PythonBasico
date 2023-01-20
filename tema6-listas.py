
nombres = ["Juan","Mario","Laura"]
numeros = [1,2,3,4,5,]

datos = [1,2,5,"Mario",True]

nombres[0] = "Roberto"

print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])
print(nombres[0])

nombres.append("Dario")
print(nombres)
nombres.insert(2, "laura")
print(nombres)

nombres.extend("checha","teofila")
print(nombres)

nombres.extend(["checha",2,23,5])
nombres.remove("checha")
print(nombres)
nombres.pop()
print(nombres)

n=["juan"]
n2=n*5
print(n2)
print(nombres)

del nombres[0]
print(nombres)