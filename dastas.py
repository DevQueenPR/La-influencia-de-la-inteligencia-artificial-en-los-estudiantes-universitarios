temperaturas = [] # define de array

for i in range(12): # read 12 values
    message = f'Entre la temperatura #{i+1}: '
    temperaturas.append( float( input(message) ) ) # append in array

print(f'La temperatura máxima es {max(temperaturas)}') # get max value
