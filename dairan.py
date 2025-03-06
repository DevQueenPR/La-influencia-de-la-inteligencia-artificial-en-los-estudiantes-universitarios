
listaTemp = []

for i in range(1, 13):
    temperatura = int(input(f"Entre la temperatura #{i}: "))
    listaTemp.append(temperatura)
print(f"\nLa temperatura mayor fue: {max(listaTemp)}")
