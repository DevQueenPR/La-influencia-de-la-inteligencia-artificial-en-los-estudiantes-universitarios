import timeit 

# Define los argumentos para el Time it
temperaturas = []
listaTemp = []
temperatura = 0
message = ''

#Funciones de cada uno 

#Enfoque 1: (AI)
def ai(temperaturas):
   
    temperaturas = [float(input(f"Temperatura del mes {i+1}: ")) for i in range(12)]

    print(f"La temperatura más alta es {max(temperaturas)} grados.")
    return temperaturas

# Enfoque 2: (estudiante)
def estudiante(listaTemp, temperatura): 

    listaTemp = []

    for i in range(1, 13):
        temperatura = int(input(f"Entre la temperatura #{i}: "))
        listaTemp.append(temperatura)
    print(f"\nLa temperatura mayor fue: {max(listaTemp)}")

    return listaTemp
   
# Enfoque 3: (profesor)
def profesor(temperaturas, message):

    temperaturas = [] # define de array

    for i in range(12): # read 12 values
        message = f'Entre la temperatura #{i+1}: '
        temperaturas.append( float( input(message) ) ) # append in array

    print(f'La temperatura máxima es {max(temperaturas)}') # get max value

    return temperaturas

# Medir el tiempo de ejecución del Enfoque 1
ai_tiempo = timeit.timeit(lambda: ai(temperaturas), number=10000) 
print("Enfoque 1: ", ai_tiempo) 
 
# Medir el tiempo de ejecución del Enfoque 2 
estudiante_tiempo = timeit.timeit(lambda: estudiante(listaTemp, temperatura), number=10000) 
print("Enfoque 2: ", estudiante_tiempo) 

# Medir el tiempo de ejecución del Enfoque 3
profesor_tiempo = timeit.timeit(lambda: profesor (temperaturas, message), number=10000) 
print("Enfoque 1: ", profesor_tiempo) 
 

#Medir el enfoque en menor a mayor
valores = [ai_tiempo, estudiante_tiempo, profesor_tiempo]
valores.sort()

menor_tiempo = valores[0]
medio_tiempo = valores[1] #cambiar nombre
mayor_tiempo = valores[2]



