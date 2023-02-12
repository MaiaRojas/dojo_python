class SLNode:
  def __init__(self, val, next=None):
    self.value = val
    self.next = next

class SList:
  def __init__(self):
    self.head = None
  
  def add_to_front(self, val):
    new_node = SLNode(val)
    current_head = self.head
    new_node.next = current_head
    self.head = new_node
    return self

  def print_values(self):
    runner = self.head
    while (runner != None):
      print(runner.value)
      runner = runner.next
    return self
  
  def add_to_back(self, val):
    if self.head == None:
      self.add_to_front(val)
      return self
    new_node = SLNode(val)
    runner = self.head
    while (runner.next != None):
      runner = runner.next
    runner.next = new_node
    return self
  
  def remove_from_front(self):
    if self.head is not None:
      self.head = self.head.next
    return self

  def print_values(self):
    runner = self.head
    while (runner != None):
      print(runner.value)
      runner = runner.next
    return self
  
  def remove_from_back(self):
    current = self.head
    previous =  None
    while current.next is not None:
      previous = current
      current =  current.next
    if previous is not None:
      previous.next = None
    else:
      self.head = None
    return self

  def remove_val(self, value):
    current = self.head
    previous =  None
    while current is not None:
      if current.value == value:
        if previous is not None:
          previous.next = current.next
        else: 
          self.head = current.next
        return self
      previous = current
      current = current.next
    return self

  def insert_at(self, value, n):
    current = self.head
    previous = None
    current_position = 0
    while current is not None and current_position < n:
      previous = current
      current = current.next
      current_position += 1

    new_node = SLNode(value, current)
    if previous is not None:
      previous.next = new_node
    else:
      self.head = new_node
    return self


my_list = SList()	# crea una nueva instancia de una lista
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("divertidas!").add_to_back("y").add_to_back("algo complejas de entender").print_values()# encadenando, yeah!
print(50*'*')
my_list.remove_from_front().print_values()
print(50*'*')
my_list.remove_from_back().print_values()
print(50*'*')
my_list.remove_val("y").print_values()
print(50*'*')
my_list.insert_at("dificiles y", 1).print_values()
# la salida debería ser:
# Las listas enlazadas
# son
# divertidas!

