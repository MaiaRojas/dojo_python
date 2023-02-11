import uuid

class Product:
  def __init__(self, name, price, category):
    self.id = str(uuid.uuid1())
    self.name = name
    self.price = price
    self.category = category

  def updatePrice(self, changePercentage, isHight):
    percentage = (self.price * changePercentage) / 100
    if isHight:
      self.price += percentage
    else:
      self.price -= percentage
    return self

  def printInfo(self):
    print(f'Produc: {self.name}, Id: {self.id}, Price: {self.price}, Category: {self.category}')
    return self

