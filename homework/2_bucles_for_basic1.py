# Basic 1


#1_Basic
for i in range(151):
  print(i)

#2_Multiplos de cinco
for i in range(5, 1000):
  if i % 5 == 0:
    print(i)

# 3_Contar, a la manera de Dojo
for i in range(100):
  if i % 10 == 0:
    print('Coding Dojo')
  elif i % 5 == 0:
    print('Coding')

#4_whoa. Es un gran idiota
total = 0
for i in range(0, 500):
  if i % 2 != 0:
    total = total + i
    print(i)

print('Total', total)

#5_cuenta regresiva de a 4
count = 2018
while count > 0:
  print(count)
  count = count - 4

#6_Contador_flexible
def searchMult(low, high, mult):
  print('Entra a la function')
  for i in range(low, high + 1):
    if i % mult == 0:
      print(i)

searchMult(2, 9 ,3)







