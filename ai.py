# Definir los meses del año
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Inicializar la lista de temperaturas
temperaturas = [0]*12

# Solicitar las temperaturas al usuario
for i in range(12):
    temperaturas[i] = float(input(f'Ingrese la temperatura para {meses[i]}: '))

# Encontrar la temperatura más alta y su correspondiente mes
temp_max = max(temperaturas)
mes_max = meses[temperaturas.index(temp_max)]

print(f'La temperatura más alta es {temp_max} y ocurrió en {mes_max}.')
