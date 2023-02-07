# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()

class Ninja:
  def __init__(self, name, lastName, treats, pet_food, pet):
    self.name = name
    self.lastName = lastName
    self.treats = treats
    self.pet_food = pet_food
    self.pet = pet


#walk(): the ninja's pet invoking the pet play() method
  def walk(self):
    self.pet.play()
    return self
# Feed(): the ninja's pet invoking the pet eat() method
  def feed(self):
    if len(self.pet_food) > 0:
      food = self.pet_food.pop()
      print(f'Feeding {self.pet.name} {food}')
      self.pet.eat()
    else:
      print('Oh no !! You need more pet food')
    return self
    
#walk(): the ninja's pet invoking the pet noise() method 
  def wash(self):
    self.pet.noise()

# implementa __init__( name , tipo , golosinas ):
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
# jugar() - incrementa la salud de la mascota en 5
# ruido() - imprime el sonido que produce la mascota

class Pet:
  def __init__(self, name, typePet, tricks, noise):
    self.name = name
    self.typePet = typePet
    self.tricks = tricks
    self.noise = noise
    self.health = 100
    self.energy = 50

  def sleep(self):
    self.energy += 25
    return self

  def eat(self):
    self.energy += 5
    self.health += 10
    return self
  
  def play (self):
    self.energy -= 15
    self.health += 5
    return self
  
  def make_noise(self):
    print(self.noise)

my_treats = ['bacon', 'chicken', 'soup']
my_pet_food = ['coki', 'soup']

fido = Pet('fido', 'dog', ['is quickly', 'is eating fast'], 'Shh, Shh')

sara = Ninja('Maia', 'Rojas', my_treats, my_pet_food, fido)

sara.feed()
sara.feed()
sara.feed()



