# Ejercicio de User

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance_account = 0
    #Agregando metodos
  def makeDeposit(self, amount):
    self.balance_account += amount
    return self

  def withDraw(self, amount):	# toma un argumento que es el monto del depósito
    self.balance_account -= amount
    return self

  def showBalance(self):
    print(f'User: {self.name}, Balance: {self.balance_account}')

  def transferMoney(self, other_user, amount):
    self.balance_account -= amount
    other_user.makeDeposit(amount)

adrien = User('Adrien', 'adrien@gmail.com') # Start with 305
nibbles = User('Mr. Nibbles', 'nibbles@gmail.com') # Start with 1200
benny = User('Benny Bob', 'benny@gmail.com') # Start with -7500

# Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
adrien.makeDeposit(100).makeDeposit(100).makeDeposit(205).withDraw(100).showBalance() #305
# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
nibbles.makeDeposit(600).makeDeposit(800).withDraw(100).withDraw(100).showBalance() #1200
# Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
benny.makeDeposit(500).withDraw(4000).withDraw(2000).withDraw(2000).showBalance()#-7500

# User Nibles transfer money 400 to User Adrien 
# BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera
# dinero al tercer usuario y luego imprime los balances de ambos usuarios
nibbles.transferMoney(adrien, 400)
nibbles.showBalance() #800
adrien.showBalance() #705
