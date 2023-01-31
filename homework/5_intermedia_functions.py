# Funciones intermedias

#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#1.1
x[1][0] = 15
print(x)

print('*'*50)
#1.2
students[1]['last_name'] = 'Bryant'
print(students)

print('*'*50)
#1.3
sports['fútbol'][0] = 'Andrés'
print(sports)

print('*'*50)
#1.4
z[0]['y'] =30
print(z)

#2. Iteraratraves de una lista de diccionarios
print('*'*50)
estudiantes = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def iterateDictionary(some_list):
  for some_dic in some_list: #{'first_name':  'Michael', 'last_name' : 'Jordan'}
    for key in some_dic.keys():
      print(f'{key} - {some_dic[key]}')

iterateDictionary(estudiantes)

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonelcopy

#3.Obtener valores de una lista de diccionarios
print('*'*50)

def iterateDictionary2(key_name, some_list):
  for value in some_list:
    print(f'{value[key_name]}')

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#4. Iterar a traves de un dictionario con valores de lista
print('*'*50)
dojo = {
  'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for some_key in some_dict:
    print(len(some_dict[some_key]), some_key.upper())
    for key in some_dict[some_key]:
      print(key)



printInfo(dojo)