class Store:
  def __init__(self, name, products = []):
    self.name = name
    self.products = products
  
  def addProduct(self, item):
    self.products.append(item)
    return self
  
  def sellProduct(self, id):
    # deleted = self.products.pop(id)
    # print (f'Produc: {deleted.name}, price: {deleted.price}, category: {deleted.category}, id: {deleted.id}')
    # return self
    for item in self.products:
      if item.id == id:
        self.products.remove(item)

    return self

  def inflation(self, rate_int):
    for item in self.products:
      item.updatePrice(rate_int, True)
    return self

  def makeLiquidation(self, category, percentage_desc):
    for item in self.products:
      if item.category == category:
        item.updatePrice(percentage_desc, False)
    return self
