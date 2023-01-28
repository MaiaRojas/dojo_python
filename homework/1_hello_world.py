# 1. TAREA: imprime "Hola, mundo"
print('Hello, world')
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print('Hola,' ,name)	# con una coma
print('Hola, '+ name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print('Hola,' ,name)	# con una coma
print('Hola,' + str(name))	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print('Amo comer {} y {}'.format(fave_food1, fave_food2)) # con .format()
print(f'Amo comer {fave_food1} y {fave_food2}') # con una cadena f

print(fave_food1.capitalize())
print(fave_food1.casefold())
print(fave_food1.center(5))
print(fave_food1.count('i'))
print(fave_food1.encode())
print(fave_food1.endswith('.'))
print(fave_food1.expandtabs(2))
print(fave_food1.find('i'))
print(fave_food1.islower())
print(fave_food1.istitle())
print(fave_food1.lower())
print(fave_food1.zfill(10))
print(fave_food1.split(','))