#1. Cuenta regresiva

def countDown(num):
  for i in range(0, int(num)+1):
    print(abs(i - num))

countDown(5)

print('*'*50)
#2.Imprimir y devolver

def printAndReturn(list):
  print(list[0])
  return list[1]

b = printAndReturn([1,2])
print(b)

print('*'*50)
#3. Primero mas longitud
def firstAntTotal(list):
  total = list[0] + len(list)
  return total

total = firstAntTotal([1,2,3,4,5])
print(total)

print('*'*50)
#4. Valores mayores que el segundo
def moreSecond(list):
  if len(list) <= 2:
    return False
  else: 
    newList=[]
    for i in list:
      if i > list[1]:
        newList.append(i)
    return newList

b = moreSecond([5,2,3,2,1,4])
c = moreSecond([3])
print(b, c)

print('*'*50)
# Esta longitud, ese valor
def lenghtAndValue(length, value):
  return [value] * length

foo = lenghtAndValue(4,7)
print(foo)
bar = lenghtAndValue(6,2)
print(bar)

