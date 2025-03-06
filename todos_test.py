import timeit 

# Define los argumentos para el Timeit
temperaturas = []
listaTemp = []
temperatura = 0
message = ''

#Enfoque 1: (AI)
def ai():
    
    # Definir los meses del año
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    # Inicializar la lista de temperaturas
    temperaturas = [0]*12

    # Solicitar las temperaturas al usuario
    for i in range(12):
        temperaturas[i] = float(89.5)

    # Encontrar la temperatura más alta y su correspondiente mes
    temp_max = max(temperaturas)
    mes_max = meses[temperaturas.index(temp_max)]

    return(f'La temperatura más alta es {temp_max} y ocurrió en {mes_max}.')

# Enfoque 2: (estudiante)
def estudiante(): 

    listaTemp = []

    for i in range(1, 13):
        temperatura = int(89.5)
        listaTemp.append(temperatura)

    return (f"\nLa temperatura mayor fue: {max(listaTemp)}")
   
# Enfoque 3: (profesor)
def profesor():

    temperaturas = [] # define de array

    for i in range(12): # read 12 values
        #message = f'Entre la temperatura #{i+1}: '
        temperaturas.append( float( 89.5) ) # append in array

    return (f'La temperatura máxima es {max(temperaturas)}')

# Medir el tiempo de ejecución del Enfoque 1
ai_tiempo = timeit.timeit(lambda: ai(), number=1000000) 
print("Enfoque 1 (A.I.): ", ai_tiempo) 
 
# Medir el tiempo de ejecución del Enfoque 2 
estudiante_tiempo = timeit.timeit(lambda: estudiante(), number=1000000) 
print("Enfoque 2 (Est.): ", estudiante_tiempo) 

# Medir el tiempo de ejecución del Enfoque 3
profesor_tiempo = timeit.timeit(lambda: profesor(), number=1000000) 
print("Enfoque 3 (Prof): ", profesor_tiempo) 



#Medir el enfoque en menor a mayor
valores = [ai_tiempo, estudiante_tiempo, profesor_tiempo]
valores.sort()

print(valores[0])
print(valores[1]) 
print(valores[2])



